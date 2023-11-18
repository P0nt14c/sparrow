# head.py
# Author: Jason Howe
# handles head requests for sparrow
import sys
sys.path.append("../")

import response
import request

def parse(request: request.Request) -> response.Response:
    # checks handled by main:
    # - version, file exists, method

    # we should check
    # access/authorization -- future work
    # last modification time
    # content type, content length

    # make response
    response = response.return_200()