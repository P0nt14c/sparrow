# response.py
# Author: Jason Howe
# Builds HTTP responses

import datetime

"""
Headers:
date
server
content-type
"""

class response:
    """ Response Class

    Attributes
    ------
    code
        the response code and reason phrase
    version
        http version string
    headers
        the http headers for the response
    body
        the body for the response
    """
    code = str
    version = str
    headers = dict
    body = str

    def __init__(self, code: str, version: str, headers: list, body: str):
        self.code = code
        self.version = version
        self.headers = headers
        self.body = body


    def __str__(self):
        resp =  self.version + " " + self.code + "\r\n"
        for key in self.headers:
            resp += key.upper() + ": " + self.headers[key] + "\r\n"
        resp += "\r\n"
        resp += self.body
        return resp


# builds a HTTP 200 reponse code
def return_200() -> response:
    """ Creates a 200 Response 

    Returns
    -------
    response
        containing 200 HTTP Code
    """ 
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    body = "Sparrow OK"
    resp = response("200 OK", "HTTP/1.1", resp_headers, body)
    return resp


# builds a HTTP 400 repsonse code
def return_400() -> response:
    """ Creates a 400 Response 

    Returns
    -------
    response
        containing 400 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    body = "Sparrow Bad Request"
    resp = response("400 Bad Request", "HTTP/1.1", resp_headers, body)
    return resp


# builds a HTTP 500 response code
def return_500() -> response:
    """ Creates a 500 Response 

    Returns
    -------
    response
        containing 500 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    body = "Sparrow Internal Server Error"
    resp = response("500 Internal Server Error", "HTTP/1.1", resp_headers, body)
    return resp

