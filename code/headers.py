# headers.py
# Author: Jason Howe
# Handles Request and Response Headers

# TODO: create method for validating general headers, entity headers, etc
def validate_request_headers(headers: dict) -> bool:
    valid_headers = ["Accept",
                    "Accept-Charset",
                    "Accept-Encoding",
                    "Accept-Language",
                    "Authorization",
                    "Cache-Control",
                    "Connection",
                    "Date",
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
                    "Trailer",
                    "Transfer-Encoding",
                    "Upgrade",
                    "User-Agent",
                    "Via",
                    "Warning"
    ]
    for key in headers:
        if key not in valid_headers:
            return False
    return True