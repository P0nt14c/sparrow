# Sparrow.py
# Author: Jason Howe
# A Functional HTTP Server, written in python

import sys
import os

import config
import comms
import request
import response
import logger
import socket
import threading
import get, delete, head, post, put


def parser_handler(req: request.Request) -> response.Response:
    print("[+] Recieved Request. Beginning Parse")
    ver_check = request.validate_version(req.version)
    if ver_check != True:
        res = response.return_505()
        logger.log("BAD", req, res)
        return res
    print("[+] Version Check Passed")

    if req.method.upper() in ["GET", "HEAD", "DELETE"]:
        page_check = request.validate_page(req.page.split("?")[0])
        if page_check != True:
            res = response.return_404()
            logger.log("BAD", req, res)
            return res
        print("[+] Page Check Passed")

    method_check = request.validate_method(req.method)
    if method_check != True:
        res = response.return_501()
        logger.log("BAD", req, res)
        return res
    print("[+] Method Check Passed")

    if req.method == "GET":
        res = get.parse(req)
        print(res)
    elif req.method == "POST":
        res = post.parse(req)
    elif req.method == "PUT":
        res = put.parse(req)
    elif req.method == "DELETE":
        res = delete.parse(req)
    elif req.method == "HEAD":
        res = head.parse(req)

    logger.log("GOOD", req, res)
  
    print("[+] Request Parsed")
    return res

def check_file(filepath) -> bool:
    # ensure file exists
    if not os.path.exists(filepath):
        return False
    # ensure file is readable
    if not os.access(filepath, os.R_OK):
        return False
    # things are good
    return True


def parse_cli(args: list) -> list:
    if len(args) == 2:
        print("[+] Entering File Mode")
        config.MODE = config.Server_Mode.FILE
    elif len(args) == 3:
        print("[+] Entering Server Mode Using HTTP")
        config.MODE = config.Server_Mode.HTTP
    elif len(args) == 5:
        print("[+] Entering Server Mode Using HTTPS")
        config.MODE = config.Server_Mode.HTTPS
    else:
        usage()
        
    if config.MODE == config.Server_Mode.FILE:
        if not check_file(args[1]):
            print("[-] Error Reading HTTP Request File. Check file path and file permissions.\n"\
                  "[-] Exiting Sparrow\n")
            sys.exit(1)
        return

    elif config.MODE == config.Server_Mode.HTTP:
        # nothing to check for HTTPS
        # set config options
        config.IP = args[1]
        config.PORT = int(args[2])
        return

    elif config.MODE == config.Server_Mode.HTTPS:
        # do HTTPS stuff here
        if not check_file(args[3]):
            print("[-] Error Reading HTTPS Public Key File. Check file path and file permissions.\n"\
                  "[-] Exiting Sparrow\n")
            sys.exit(1)
        elif not check_file(args[4]):
            print("[-] Error Reading HTTPS Public Key File. Check file path and file permissions.\n"\
                  "[-] Exiting Sparrow\n")
            sys.exit(1)
        
        # set config options
        config.IP = args[1]
        config.PORT = int(args[2])
        config.CERTFILE = args[3]
        config.KEYFILE = args[4]
        return


def usage():
    print("[-] CLI Argument Error.\n"\
          "[-] To use file mode: python3 sparrow.py <path/to/file>\n"\
          "[-] To use HTTP Server mode: python3 sparrow.py <ip> <port>\n"\
          "[-] To use HTTPS Server mode: python3 sparrow.py <ip> <port> <pub key> <priv key>\n"\
          "[+] Exiting Sparrow\n"
          )
    sys.exit(1)


def handle_client(conn: socket):
    print("[+] Client Connected. Thread Started")
    reqdata = comms.recieve(conn)
    print("[+] Connected Recieved")
    _, req = request.parse(reqdata)
    print("[+] Request Received")
    res = parser_handler(req)
    print("[+] Response Built")
    print(res)
    comms.send(conn, res.__str__())
    print("[+] Response Sent")
    return


if __name__ == "__main__":
    # parse/validate CLI input
    print("[+] Starting Sparrow Web Server")
    print("[+] Initializing Logger")
    logger.init_logger()
    print("[+] Logger Initialized")
    print("[+] Parsing CLI Arguements")
    args = parse_cli(sys.argv)
    print("[+] CLI Arguements Parsed")
    
    try:
        if config.MODE == config.Server_Mode.FILE:
            with open(sys.argv[1]) as req_file:
                req = req_file.read()
                res = parser_handler(req)
                print(res)
        elif config.MODE == config.Server_Mode.HTTP:
            # create connection
            sock = comms.create_socket()
            
            while True:
                # recieve connections
                conn, addr = sock.accept()
                # create thread to handle connection
                client_thread = threading.Thread(target=handle_client, args=(conn,))
                client_thread.start()
            
        elif config.MODE == config.Server_Mode.HTTPS:
            # create connection
            sock = comms.create_secure_socket()
            
            while True:
                # recieve connections
                conn, addr = sock.accept()
                # create thread to handle connection
                client_thread = threading.Thread(target=handle_client, args=(conn,))
                client_thread.start()
    except KeyboardInterrupt:
        print("[+] Shutting down Sparrow")
    finally:
        sock.close()

    print("[+] Sparrow Shut Down")
    
    