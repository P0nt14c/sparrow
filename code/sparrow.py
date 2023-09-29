# Sparrow.py
# Author: Jason Howe
# A Functional HTTP Server, written in python

import sys
import request
import response
import logger

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


def usage():
    print("Sparrow Web Server\n"\
          "To use file mode: python3 sparrow.py <path/to/file>\n"\
          "To use HTTP Server mode: python3 sparrow.py <ip> <port>\n"
          "To use HTTPS Server mode: python3 sparrow.py <ip> <port> <pub key> <priv key>"
          )


if __name__ == "__main__":
    # check sys arg length to get mode
    if len(sys.argv) == 2:
        print("file mode")
        sys.exit(0)
    if len(sys.argv) == 3:
        print("http mode")
        sys.exit(0)
    elif len(sys.argv) == 5:
        print("https mode")
        sys.exit(0)
    else:
        usage()
        sys.exit(0)


    request_file = sys.argv[1]
    with open(request_file, "r") as rfile:
        req_str = rfile.read()
    

    err, req = request.parse(req_str)
    if err == 1:
        res = response.return_400()
        logger.log("BAD", req, res)
        sys.exit(0)
    
    parser_handler(req)
    