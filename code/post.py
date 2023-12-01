# post.py
# Author: Jason Howe
# handles post requests for sparrow


# native libraries
import os


# our imports
import response
import request

def parse(request: request.Request) -> response.Response:
    print("[+] Parsing Post")
    # checks handled by main: version, file exists, method

    # make path relatetive
    request.page = request.page.lstrip("/")
    page = os.path.join("pages", request.page)

    # access/authorization -- future work

    # content-length
    if "Content-Length" not in request.headers:
        res = response.return_411()
        return res
    

    # if file exists, delete
    file_exists = os.path.exists(page)
    if file_exists:
        os.remove(page)
    
    with open(page, "w") as dest:
        dest.write(request.body)

    if file_exists:
        res = response.return_201()
    else:
        res = response.return_200()

    print("[+] Post Parsed")
    return res