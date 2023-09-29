# config.py
# Author: Jason Howe
# config file for sparrow

from enum import Enum

# Global Variables
VERBOSE = 0
IP = "127.0.0.1"
PORT = 4862 
MODE = 0

class Server_Mode(Enum):
    FILE = 1
    HTTP = 2
    HTTPS = 3

class Response_Code(Enum):
    OK = 200
    CREATED = 201
    BADREQUEST = 400
    FORBIDDEN = 403
    NOTFOUND = 404
    LENGTHREQUIRED = 411
    INTERNAL = 500
    NOTIMPLEMENTED = 501
    HTTPVERSION = 505