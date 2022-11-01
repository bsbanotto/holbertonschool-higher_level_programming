#!/usr/bin/python3
"""
This script  takes in a URL and an email, sends a request to the passed
URL, and displays the body of the body of the response (decoded in utf-8)
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
