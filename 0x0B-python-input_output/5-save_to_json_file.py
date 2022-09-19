#!/bin/usr/python3
"""This module writes an Object to a text file using JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes my_obj to filenmame using JSON representation
    """
    with open(filename, 'a', encoding="UTF8") as newFile:
        return json.dump(my_obj, newFile)
