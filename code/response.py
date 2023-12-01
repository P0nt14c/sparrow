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

class Response:
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
            resp += str(key.upper()) + ": " + str(self.headers[key]) + "\r\n"
        resp += "\r\n"
        resp += self.body
        return resp


# builds a HTTP 200 reponse code
def return_200() -> Response:
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
    resp_headers["Connection"] = "close"
    body = "Sparrow OK"
    resp = Response("200 OK", "HTTP/1.1", resp_headers, body)
    return resp

def return_201() -> Response:
    """ Creates a 201 Response 

    Returns
    -------
    response
        containing 201 HTTP Code
    """ 
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    resp_headers["Connection"] = "close"
    body = "Sparrow OK"
    resp = Response("201 Created", "HTTP/1.1", resp_headers, body)
    return resp


# builds a HTTP 400 repsonse code
def return_400() -> Response:
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
    resp_headers["Connection"] = "close"
    body = "Sparrow Bad Request"
    resp = Response("400 Bad Request", "HTTP/1.1", resp_headers, body)
    return resp

# builds a HTTP 403 repsonse code
def return_403() -> Response:
    """ Creates a 403 Response 

    Returns
    -------
    response
        containing 403 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    resp_headers["Connection"] = "close"
    body = "Sparrow OK. Client Bad Request"
    resp = Response("403 Forbidden", "HTTP/1.1", resp_headers, body)
    return resp


# builds a HTTP 404 repsonse code
def return_404() -> Response:
    """ Creates a 404 Response 

    Returns
    -------
    response
        containing 404 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    resp_headers["Connection"] = "close"
    body = "Sparrow OK. Client Bad Request"
    resp = Response("404 Not Found", "HTTP/1.1", resp_headers, body)
    return resp

# builds a HTTP 411 repsonse code
def return_411() -> Response:
    """ Creates a 4011 Response 

    Returns
    -------
    response
        containing 411 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    resp_headers["Connection"] = "close"
    body = "Sparrow OK. Client Bad Request"
    resp = Response("411 Length Required", "HTTP/1.1", resp_headers, body)
    return resp


# builds a HTTP 500 response code
def return_500() -> Response:
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
    resp_headers["Connection"] = "close"
    body = "Sparrow Internal Server Error"
    resp = Response("500 Internal Server Error", "HTTP/1.1", resp_headers, body)
    return resp


# builds a HTTP 501 response code
def return_501() -> Response:
    """ Creates a 501 Response 

    Returns
    -------
    response
        containing 501 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    resp_headers["Connection"] = "close"
    body = "Sparrow Internal Server Error"
    resp = Response("501 Not Implemented", "HTTP/1.1", resp_headers, body)
    return resp

# builds a HTTP 505 response code
def return_505() -> Response:
    """ Creates a 505 Response 

    Returns
    -------
    response
        containing 505 HTTP Code
    """
    resp_headers = dict()
    resp_headers["Server: "] = "Sparrow"
    resp_headers["Date: "] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %Z")
    resp_headers["Content-type: "] = "text/plain"
    resp_headers["Connection"] = "close"
    body = "Sparrow Internal Server Error"
    resp = Response("505 HTTP Version Not Supported", "HTTP/1.1", resp_headers, body)
    return resp