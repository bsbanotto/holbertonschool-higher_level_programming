#!/usr/bin/python3
"""
This script takes in a letter(argv[1]), and sends a POST request
to http://0.0.0.0:5000/search_user
The letter is sent in the variable q
If no argument is given, q = ""
If the response is properly JSON formatted and not empty, display[<id>] <name>
Otherwise
- Display "Not a valid JSON" if JSON is invalid
- Display "No result" if the JSON is empty
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    req = requests.post(url, data={'q': q})
    try:
        dict = req.json()
        id = dict.get('id')
        name = dict.get('name')
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception as e:
        print("Not a valid JSON")
