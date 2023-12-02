# delete.py
# Author: Jason Howe
# handles delete requests for sparrow

# native libraries
import os

# our imports
import response
import request

def parse(request: request.Request) -> response.Response:
    
    # make path relatetive
    request.page = request.page.lstrip("/")
    page = os.path.join("pages_tmp", request.page)

    try:
        os.remove(page)
        res = response.return_200()
    except:
        res = response.return_500()

    return res
