# headers.py
# Author: Jason Howe
# Handles Request and Response Headers

GENERAL_HEADERS = [
    "Cache-Control",
    "Connection",
    "Date",
    "Pragma",
    "Trailer",
    "Transfer-Encoding",
    "Upgrade",
    "Via",
    "Warning"
]

REQUEST_HEADERS = [
    "Accept",
    "Accept-Charset",
    "Accept-Encoding",
    "Accept-Language",
    "Authorization",
    "Expect",
    "From",
    "Host",
    "If-Match",
    "If-Modified-Since",
    "If-None-Match",
    "If-Range",
    "If-Unmodified-Since",
    "Max-Forwards",
    "Pragma",
    "Proxy-Authorization",
    "Range",
    "Referer",
    "TE" ,
    "User-Agent",
]

RESPONSE_HEADERS = [
    "Accept-Ranges",
    "Age",
    "ETag",
    "Location",
    "Proxy-Atuenticate",
    "Retry-After",
    "Server",
    "Vary",
    "WWW-Authenticate"
]

ENTITY_HEADERS = [
    "Allow",
    "Content-Encoding",
    "Content-Language",
    "Content-Length",
    "Content-Location",
    "Content-MD5",
    "Content-Range",
    "Expires",
    "Last-Modified",

]


def validate_request_headers(headers: dict) -> bool:
    

    # header dicts
    general_headers = {}
    request_headers = {}
    entity_headers = {}
    discard_headers = {}

    # run thru all of the headers. lump headers into different dicts
    for hname in headers:
        if hname in GENERAL_HEADERS:
            general_headers[hname] = headers[hname]
        elif hname in REQUEST_HEADERS:
            request_headers[hname] = headers[hname]
        elif hname in ENTITY_HEADERS:
            entity_headers[hname] = headers[hname]
        else:
            discard_headers[hname] = headers[hname]


def validate_general_headers(gheaders: dict):
    #cache control
    if "Cache-Control" in gheaders:
        if gheaders["Cache-Control"] != "no-cache":
            # do something to return error code here
            pass 
    
    # Connection
    if "Connection" in gheaders:
        if gheaders["Connection"] != "close":
            # do something to return error code here
            pass 
    
    # Date
    if "Date" in gheaders:
        # maybe do something to check if request type is POST or PUT 
        pass

    # Pragma
    if "Pragma" in gheaders:
        if gheaders["Cache-Control"] != "no-cache":
            # do something to return error code here
            pass 

    # Trailer // TODO implement a check for trailers
    if "Trailer" in gheaders:
        pass

    # Transfer-Encoding
    if "Transfer-Encoding" in gheaders:
        if gheaders["Transfer-Encoding"] == "chunked":
            # do something here // return 501 not implemented
            pass
        elif gheaders["Transfer-Encoding"] == "identity":
            # do something here // return 501 not implemented
            pass
        elif gheaders["Transfer-Encoding"] == "gzip":
            # do something here // return 501 not implemented
            pass
        elif gheaders["Transfer-Encoding"] == "compress":
            # do something here // return 501 not implemented
            pass
        elif gheaders["Transfer-Encoding"] == "deflate":
            # do something here // return 501 not implemented
            pass

    # Upgrade
    if "Upgrade" in gheaders:
        # do something
        pass

    # Via
    if "Via" in gheaders:
        # do something
        pass

    # Warning
    if "Warning" in gheaders:
        # do something
        pass

    