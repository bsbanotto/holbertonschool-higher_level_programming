#!/usr/bin/python3
"""
This script takes GitHub credentials and uses the GitHub API do display my id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    req = requests.get(url, auth=HTTPBasicAuth(username, token)).json()
    print(req.get('id'))
