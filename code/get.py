# get.py
# Author: Jason Howe
# handles get requests for sparrow


# native libraries
import os
from datetime import datetime
import mimetypes
import subprocess

# our imports
import response
import request


def parse(request: request.Request) -> response.Response:
    print("[+] Parsing Get")
    
    # pass off execution of PHP
    if ".php" in request.page:
        res = handle_php(request)
        return res

    # checks handled by main: version, file exists, method

    # make path relatetive
    request.page = request.page.lstrip("/")
    page = os.path.join("pages_tmp", request.page)

    # access/authorization -- future work

    # last modification time
    file_stat = os.stat(page)
    modification_time = file_stat.st_mtime
    modification_time_str = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

    # content type, content encoding, content length
    content_length = file_stat.st_size
    content_type, content_encoding = get_file_content_type(page)
    

    # make response
    res = response.return_200()
    res.headers["Last-Modification"] = modification_time_str
    res.headers["Content-Length"] = content_length
    if content_type != "NA":
        res.headers["Content-Type"] = content_type
    if content_encoding != "NA":
        res.headers["Content-Type"] = content_encoding

    # add body contents 
    with open(page, 'r') as file:
        body = file.read()
    res.body = body

    print("[+] Get Parsed")
    return res


# returns the file type and encoding
def get_file_content_type(file_path) -> tuple:
    try:
        # Get the MIME type based on the file extension
        content_type, encoding = mimetypes.guess_type(file_path)

        if content_type is None:
            return ("NA", "NA")
        else:
            return (content_type, encoding)
    except FileNotFoundError:
        return ("NA", "NA")
    except Exception as e:
        return (f"NA", "NA")
    


def handle_php(request: request.Request) -> response.Response:
    print("[+] Parsing GET PHP")
    # make path relatetive
    request.page = request.page.lstrip("/")
    page = os.path.join("pages_tmp", request.page)

    query = page.split("?")[1]
    page = page.split("?")[0]

    params = {}
    for param in query.split('&'):
        key, value = param.split('=')
        params[key] = value
    
    php_cmd = ["pgp-cgi", "-f", page]
    if params:
        for key, value in params.items():
            php_cmd.extend(['-d', f"{key}={value}"])
    print("[+] PHP CMD: ", " ".join(php_cmd))
    
    try:
        result = subprocess.run(php_cmd, capture_output=True, text=True)
    except:
        res = response.return_500()
        return res
    
    # last modification time
    file_stat = os.stat(page)
    modification_time = file_stat.st_mtime
    modification_time_str = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

    # content type, content encoding, content length
    content_length = file_stat.st_size
    content_type, content_encoding = get_file_content_type(page)
    

    # make response
    res = response.return_200()
    res.headers["Last-Modification"] = modification_time_str
    res.headers["Content-Length"] = content_length
    if content_type != "NA":
        res.headers["Content-Type"] = content_type
    if content_encoding != "NA":
        res.headers["Content-Type"] = content_encoding


    # res.body = " ".join(php_cmd)
    res.body = result.stdout
    print("[+] Parsed GET PHP")
    return res
