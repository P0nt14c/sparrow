# response.py
# Author: Jason Howe
# Logs HTTP Requests and Responses

import request
import response
import datetime
import json
import os


class Log:
    """ Request Class

    Attributes
    ------
    type
        GOOD or BAD
    req 
        the request
    res
        the response
    time
        time of the log
    
    Methods
    -------
    to_dict
        returns a dictionary representation of the Log class
    """
    type = str
    req = str
    res = dict
    time = str

    def __init__(self, type: str, req: request.Request, res: response.Response) -> None:
        self.type = type
        self.req = req
        self.res = res
        self.time = str(datetime.datetime.now())

    def to_dict(self) -> dict:
        d = {}
        d["time"] = self.time
        d["type"] = self.type
        d["req"] = self.req
        d["res"] = self.res
        return d

def init_logger() -> bool:
    """ Initializes the logger 

    Paramters
    --------
    none 

    Returns
    -------
    bool
        True if the logger is set up
        False if not
    """ 
    try: 
        # delete log files
        os.remove("../log/good.txt")
        os.remove("../log/bad.txt")
        # create new log files
        goodlog = open("../log/good.txt", "x") 
        badlog = open("../log/bad.txt", "x") 
        # close files
        goodlog.close()
        badlog.close()
        return True
    except Exception:
        return False


def log(type: str, req: request.Request, res: response.Response):
    """ Logs Requests and Response 

    Paramters
    --------
    type : str
        GOOD or BAD
    req : request.Request
        the request to log 
    res : response.Reponse
        the reponse to the request to log

    Returns
    -------
    None
    """ 
    # set type to BAD if it's isn't GOOD.
    if type != "GOOD":
        type = "BAD"

    # create an instance of Log type
    log = Log(type, str(req), str(res))

    # create a JSON string to log
    json_log = json.dumps(log.to_dict())

    # write log to file
    if type == "GOOD":
        with open("../log/good.txt", "+a") as logfile:
            logfile.write(json_log)
    else:
        with open("../log/bad.txt", "+a") as logfile:
            logfile.write(json_log)
