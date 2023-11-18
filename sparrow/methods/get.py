# get.py
# Author: Jason Howe
# handles get requests for sparrow

# import functions from the upper dictionary
import sys
sys.path.append("../")

# native libraries
import os
import datetime
import mimetypes

# our imports
import response
import request


def parse(request: request.Request) -> response.Response:
    # checks handled by main: version, file exists, method

    # access/authorization -- future work

    # last modification time
    file_stat = os.stat(request.page)
    modification_time = file_stat.st_mtime
    modification_time_str = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')

    # content type, content encoding, content length
    content_length = file_stat.st_size
    content_type, content_encoding = get_file_content_type(request.page)
    

    # make response
    response = response.return_200()
    response.headers["Last-Modification"] = modification_time_str
    response.headers["Content-Length"] = content_length
    if content_type != "NA":
        response.headers["Content-Type"] = content_type
    if content_encoding != "NA":
        response.headers["Content-Type"] = content_encoding

    # add body contents 
    with open(request.body, 'r') as file:
        body = file.read()
    response.body = body


    return response


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