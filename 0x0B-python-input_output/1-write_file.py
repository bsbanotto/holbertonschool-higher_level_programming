#!/usr/bin/python3
"""This module writes a string of text to a file and returns
number of characters written
"""


def write_file(filename="", text=""):
    """Given a filename and text string, write that text to that file
    Return the number of characters written
    """
    with open(filename, "w", encoding="UTF8") as newFile:
        newFile.write(text)
        charNum = 0
        for char in text:
            charNum += 1

    return(charNum)
