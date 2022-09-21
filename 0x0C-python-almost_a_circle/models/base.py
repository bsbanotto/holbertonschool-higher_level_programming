#!/usr/bin/python3
"""
This is the base module for the Almost A Circle package
"""
import json


class Base:
    """
    This is the base class for the Almost A Circle package
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initiate the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Method to return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        elif len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
