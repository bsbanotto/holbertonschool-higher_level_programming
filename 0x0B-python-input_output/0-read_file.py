#!/usr/bin/python3
"""This module reads text from a file and prints to stdout
"""


def read_file(filename=""):
    """Given a filename, print to stdout
    """
    with open(filename, encoding="utf=8") as file:
        text = file.read()
        print(text, end="")