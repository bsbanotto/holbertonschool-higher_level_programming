#!/usr/bin/python3
"""
This script lists the 10 most recent commits on GitHub
Repository given as argv[1] = 'rails'
User given as argv[2] = 'rails'
Print all commits by: `<sha>: <author name>` (one by line)
"""
import requests
import sys


if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    req = requests.get(url)
    text_file = req.json()
    for item in text_file[:10]:
        print("{}: {}".format(item.get('sha'), item.get('commit')
                              .get('author').get('name')))