#!/usr/bin/python3
"""This module returns the JSON representation of a string object
"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of the provided object
    """
    jsonString = json.dumps(my_obj)
    return(jsonString)