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
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    # print(url)

    req = requests.get(url)
    text_file = req.json()
    for commit in text_file[0:10]:
        print("{}: {}".format(commit.get('sha'), commit.get('commit')
                              .get('author').get('name')))
