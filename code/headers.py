# headers.py
# Author: Jason Howe
# Handles Request and Response Headers

GENERAL_HEADERS = [
    "Cache-Control",
    "Connection",
    "Date",
    "Pragma",
    "Trailer",
    "Trasnfer-Encoding",
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




    