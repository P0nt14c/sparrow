# response.py
# Author: Jason Howe
# Receives HTTP requests


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
    host = str
    headers = dict
    body = str


    def __init__(self, method, page, version, host, headers, body):
        self.method = method
        self.page = page
        self.version = version
        self.host = host
        self.headers = headers
        self.body = body


    def __str__(self):
        req = self.method + " " + self.page + " " + self.version + "\r\n"
        req += "Host: " + self.host + "\r\n"
        for key in self.headers:
            req += key.upper() + ": " + self.headers[key] + "\r\n"
        req += "\r\n"
        req += self.body
        return req


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
    

def validate_page(page: str, pages: list) -> bool:
    """ Validates the Page in the HTTP Request

    Paramters
    --------
    page : str
        the method to validate
    pages : list
        the list of pages served

    Returns
    -------
    bool
        True if the page exists
        False if not
    """ 
    if page in pages:
        return True
    else:
        return False
    

