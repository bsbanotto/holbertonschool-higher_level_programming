#!/usr/bin/python3
"""This module returns the dictionary description fo JSON
serialization of an object
"""


def class_to_json(obj):
    """This function does the work of this module
    """
    return vars(obj)
