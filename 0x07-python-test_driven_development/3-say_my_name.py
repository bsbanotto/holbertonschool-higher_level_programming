#!/usr/bin/python3
"""This will repeate given names back to us
"""


def say_my_name(first_name, last_name=""):
    """First name must be privided as a string
       Last name, when provided, must be a string
       If no last name is provided, it will be empty string
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if len(last_name) > 0:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
