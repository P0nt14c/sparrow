# Sparrow.py
# Author: Jason Howe
# A Functional HTTP Server, written in python

import sys
import os

import request
import response
import logger
import config


def parser_handler(req: request.Request) -> response.response:

    ver_check = request.validate_version(req.version)
    if ver_check != True:
        res = response.return_400()
        logger.log("BAD", req, res)
        return

    page_check = request.validate_page(req.page)
    if page_check != True:
        res = response.return_400()
        logger.log("BAD", req, res)
        return

    method_check = request.validate_method(req.method)
    if method_check != True:
        res = response.return_400()
        logger.log("BAD", req, res)
        return

    if req.method == "GET":
        err = request.parse_get(req)
    elif req.method == "POST":
        err = request.parse_post(req)
    elif req.method == "PUT":
        err = request.parse_put(req)
    elif req.method == "DELETE":
        err = request.parse_delete(req)
    elif req.method == "HEAD":
        err = request.parse_head(req)

    if err == 0:
        res = response.return_200()
        logger.log("GOOD", req, res)
        return
    elif err == 1:
        res = response.return_400()
        logger.log("BAD", req, res)
        return
    elif err == 2:
        res = response.return_500()
        logger.log("BAD", req, res)
        return

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
        # do HTTP stuff here
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
        return


def usage():
    print("[-] CLI Argument Error.\n"\
          "[-] To use file mode: python3 sparrow.py <path/to/file>\n"\
          "[-] To use HTTP Server mode: python3 sparrow.py <ip> <port>\n"\
          "[-] To use HTTPS Server mode: python3 sparrow.py <ip> <port> <pub key> <priv key>\n"\
          "[+] Exiting Sparrow\n"
          )
    sys.exit(1)



if __name__ == "__main__":
    # parse/validate CLI input
    print("[+] Starting Sparrow Web Server")
    print("[+] Parsing CLI Arguements")
    args = parse_cli(sys.argv)
    print("[+] CLI Arguements Parsed")
    print("[+] Initializing Logger")
    logger.init_logger()
    print("[+] Logger Initialized")

    
    # parser_handler(req)
    