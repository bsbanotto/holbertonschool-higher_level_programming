#!/usr/bin/python3
"""This module will append text to the end of a file
"""


def append_write(filename="", text=""):
    """Given a file, filename, append given text string to end
    If the given file dosn't exist, it should be created
    """
    with open(filename, "a", encoding="UTF8") as appendFile:
        appendFile.write(text)
        charNum = 0
        for char in text:
            charNum += 1
    return charNum
