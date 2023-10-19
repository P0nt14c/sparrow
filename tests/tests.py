# config.py
# Author: Jason Howe
# Testing file for Sparrow

import requests

# TEST CASE:
# Regular Requests

SPARROW_TEST_URL = "http://127.0.0.1"
SPARROW_TEST_PORT = 80

CASES = {
    "Bad_Method": "Tests the servers handling of non-standard methods",
    "GET": "Tests GET request with existing file",
    "GET_Bad_File": "Tests GET request with non-existant file",
    "GET_Bad_Params": "Tests GET request with invalid parameters",
    "POST": "Tests POST request with existing file",
    "POST_Bad_File": "Tests POST request with non-existant file",
    "POST_Bad_Params": "Tests POST with invalid parameters"
}

def print_result(success: bool, name: str) -> None:
    if success:
        print("Test Case: {} Passed. {}".format(name, CASES[name]))
    else:
        print("Test Case: {} Failed. {}".format(name, CASES[name]))


def test_bad_method():
    r = requests.request("NAH", SPARROW_TEST_URL)
    if r.status_code != 400:
        print_result(False, "Bad_Method")
    else:
        print_result(True, "Bad_Method")


def test_get():
    # Normal Get Request
    r = requests.get(SPARROW_TEST_URL+"test.html")
    if r.status_code != 200:
         print_result(False, "GET")
    else:
        print_result(True, "GET")
    
    # Get Request on non-existant file
    r = requests.get(SPARROW_TEST_URL+"thisdoesntexist.html")
    if r.status_code != 404:
         print_result(False, "GET_Bad_File")
    else:
        print_result(True, "GET_Bad_File")

    # Normal Get Request With Params
    r = requests.get(SPARROW_TEST_URL+"test.html", params={"locale": "New York"})
    if r.status_code != 200: # unsure what code this should be yet
         print_result(False, "GET_Bad_Params")
    else:
        print_result(True, "GET_Bad_Params")


def test_post():
    # Normal Post Request
    r = requests.post(SPARROW_TEST_URL+"test.html")
    if r.status_code != 200:
         print_result(False, "POST")
    else:
        print_result(True, "POST")

    # Post Request on non-existant file
    r = requests.post(SPARROW_TEST_URL+"thisdoesntexist.html")
    if r.status_code != 404:
         print_result(False, "POST_Bad_File")
    else:
        print_result(True, "POST_Bad_File")

    # Post Get Request With Params
    r = requests.post(SPARROW_TEST_URL+"test.html", params={"locale": "New York"})
    if r.status_code != 200: # unsure what code this should be yet
         print_result(False, "POST_Bad_Params")
    else:
        print_result(True, "POST_Bad_Params")


# def test_put():
#     # Normal PUT Request
#     r = requests.post(SPARROW_TEST_URL+"test.html") # update w/ file
#     if r.status_code != 200:
#          print_result(False, "POST")
#     else:
#         print_result(True, "POST")

#     # does this make any sense??
#     # PUT Request on non-existant file
#     r = requests.post(SPARROW_TEST_URL+"thisdoesntexist.html")
#     if r.status_code != 404:
#          print_result(False, "POST_Bad_File")
#     else:
#         print_result(True, "POST_Bad_File")

#     # does this make sense
#     # Post Get Request With Params
#     r = requests.post(SPARROW_TEST_URL+"test.html", params={"locale": "New York"})
#     if r.status_code != 200: # unsure what code this should be yet
#          print_result(False, "POST_Bad_Params")
#     else:
#         print_result(True, "POST_Bad_Params")



# def test_head():
#     # Normal PUT Request
#     r = requests.post(SPARROW_TEST_URL+"test.html") # update w/ file
#     if r.status_code != 200:
#          print_result(False, "POST")
#     else:
#         print_result(True, "POST")

#     # does this make any sense??
#     # PUT Request on non-existant file
#     r = requests.post(SPARROW_TEST_URL+"thisdoesntexist.html")
#     if r.status_code != 404:
#          print_result(False, "POST_Bad_File")
#     else:
#         print_result(True, "POST_Bad_File")

#     # does this make sense
#     # Post Get Request With Params
#     r = requests.post(SPARROW_TEST_URL+"test.html", params={"locale": "New York"})
#     if r.status_code != 200: # unsure what code this should be yet
#          print_result(False, "POST_Bad_Params")
#     else:
#         print_result(True, "POST_Bad_Params")


# def test_delete():
#     # Normal PUT Request
#     r = requests.post(SPARROW_TEST_URL+"test.html") # update w/ file
#     if r.status_code != 200:
#          print_result(False, "POST")
#     else:
#         print_result(True, "POST")

#     # does this make any sense??
#     # PUT Request on non-existant file
#     r = requests.post(SPARROW_TEST_URL+"thisdoesntexist.html")
#     if r.status_code != 404:
#          print_result(False, "POST_Bad_File")
#     else:
#         print_result(True, "POST_Bad_File")

#     # does this make sense
#     # Post Get Request With Params
#     r = requests.post(SPARROW_TEST_URL+"test.html", params={"locale": "New York"})
#     if r.status_code != 200: # unsure what code this should be yet
#          print_result(False, "POST_Bad_Params")
#     else:
#         print_result(True, "POST_Bad_Params")


# def test_options():
#     # Normal PUT Request
#     r = requests.post(SPARROW_TEST_URL+"test.html") # update w/ file
#     if r.status_code != 200:
#          print_result(False, "POST")
#     else:
#         print_result(True, "POST")

#     # does this make any sense??
#     # PUT Request on non-existant file
#     r = requests.post(SPARROW_TEST_URL+"thisdoesntexist.html")
#     if r.status_code != 404:
#          print_result(False, "POST_Bad_File")
#     else:
#         print_result(True, "POST_Bad_File")

#     # does this make sense
#     # Post Get Request With Params
#     r = requests.post(SPARROW_TEST_URL+"test.html", params={"locale": "New York"})
#     if r.status_code != 200: # unsure what code this should be yet
#          print_result(False, "POST_Bad_Params")
#     else:
#         print_result(True, "POST_Bad_Params")