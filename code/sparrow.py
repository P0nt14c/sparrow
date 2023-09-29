# Sparrow.py
# Author: Jason Howe
# A Functional HTTP Server, written in python

import sys
import request
import response

def parser_handler(req: request.Request) -> response.response:

    ver_check = request.validate_version(req.version)
    if ver_check != True:
        res = response.return_400()
        print(res) # TODO: switch to log
        return

    page_check = request.validate_page(req.page)
    if page_check != True:
        res = response.return_400()
        print(res) # TODO: switch to log
        return

    method_check = request.validate_method(req.method)
    if method_check != True:
        res = response.return_400()
        print(res) # TODO: switch to log
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
        print(res) # TODO: switch to log
        return
    elif err == 1:
        res = response.return_400()
        print(res) # TODO: switch to log
        return
    elif err == 2:
        res = response.return_500()
        print(res) # TODO: switch to log
        return


if __name__ == "__main__":
    request_file = sys.argv[1]
    with open(request_file, "r") as rfile:
        req_str = rfile.read()
    

    err, req = request.parse(req_str)
    if err == 1:
        res = response.return_400()
        print(res) # TODO: switch to log
        sys.exit(0)
    
    parser_handler(req)
    