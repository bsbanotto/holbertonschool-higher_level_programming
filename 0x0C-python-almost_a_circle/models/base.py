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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Method to return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        dicts = []
        if list_objs is not None:
            for thing in list_objs:
                dicts.append(thing.to_dictionary())
        with open(cls.__name__+".json", "w", encoding="UTF8") as newFile:
            newFile.write(cls.to_json_string(dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        This method returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            temp = cls(1, 2)
        if cls.__name__ == 'Square':
            temp = cls(42)
        temp.update(**dictionary)
        return(temp)

    @classmethod
    def load_from_file(cls):
        """
        This method returns a list of instances of objects
        """
        with open(cls.__name__+".json", "r", encoding="UTF8") as openedFile:
            if openedFile:
                file_string = openedFile.read()
                dlist = []
                for obj in cls.from_json_string(file_string):
                    dlist.append(cls.create(**obj))
                return dlist
            else:
                return []
