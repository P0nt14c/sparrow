# Sparrow.py
# Author: Jason Howe
# A Functional HTTP Server, written in python

import sys
import request
import response




if __name__ == "__main__":
    request_file = sys.argv[1]
    with open(request_file, "r") as rfile:
        req_str = rfile.read()
    

    err, req = request.parse(req_str)
    if err == 1:
        res = response.return_400()
        print(res)
    
    if req.method == "GET":
        err = request.parse_get(req)
    elif req.mtehod == "POST":
        err = request.parse_post(req)
    elif req.mtehod == "PUT":
        err = request.parse_put(req)
    elif req.mtehod == "DELETE":
        err = request.parse_delete(req)
    elif req.mtehod == "HEAD":
        err = request.parse_head(req)
    
    if err == 0:
        res = request.return_200()
        print(res)
    elif err == 1:
        res = request.return_400()
        print(res)
    elif err == 2:
        res = request.return_500()
        print(res)


    