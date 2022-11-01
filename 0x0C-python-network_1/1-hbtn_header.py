#!/usr/bin/python3
"""
This script displays the X-Request-ID from a passed in URL
"""
from urllib import request
import sys


if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as page:
        # print (page.info())
        print(page.info()['X-Request-Id'])
