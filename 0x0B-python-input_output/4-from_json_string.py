#!/usr/bin/python3
"""This module returns a Python data structure represented by a JSON string
"""
import json


def from_json_string(my_str):
    """This function returns the Python Data Structure object
    """
    myObject = json.loads(my_str)
    return(myObject)
