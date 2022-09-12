#!/usr/bin/python3
"""Inserts two new lines after special characters . ? :
"""


def text_indentation(text):
    """Testing first for valid input to function, then printing
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    text_period = text.replace(". ", ".\n\n")
    text_question = text_period.replace("? ", "?\n\n")
    text_colon = text_question.replace(": ", ":\n\n")

    print(text_colon, end="")
