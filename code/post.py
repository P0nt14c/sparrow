# post.py
# Author: Jason Howe
# handles post requests for sparrow


# native libraries
import os
import subprocess

# our imports
import response
import request

def parse(request: request.Request) -> response.Response:
    print("[+] Parsing Post")


    # content-length
    if "Content-Length" not in request.headers:
        res = response.return_411()
        return res
    

    # pass off execution of PHP
    if ".php" in request.page:
        res = handle_php(request)
        return res

    # checks handled by main: version, file exists, method

    # make path relatetive
    request.page = request.page.lstrip("/")
    page = os.path.join("pages", request.page)

    # access/authorization -- future work

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




def handle_php(request: request.Request) -> response.Response:
    print("[+] Parsing POST PHP")
    # make path relatetive
    request.page = request.page.lstrip("/")
    page = os.path.join("pages", request.page)

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
    
    # make response
    res = response.return_200()
   
    # res.body = " ".join(php_cmd)
    res.body = result.stdout
    print("[+] Parsed POST PHP")
    return res
