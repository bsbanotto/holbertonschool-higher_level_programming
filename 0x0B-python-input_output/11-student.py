#!/usr/bin/python3
"""This module defines a student class
"""


class Student():
    """Student attributes are defined here
    """
    def __init__(self, first_name, last_name, age):
        """Inistantiate the Student class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Send the Student class to json
        """
        if attrs is None:
            return vars(self)
        studentDictionary = {}
        for i in attrs:
            try:
                studentDictionary[i] = vars(self)[i]
            except:
                Exception

        return studentDictionary

    def reload_from_json(self, json):
        """This method takes information from our JSON and loads it to
        our dictionary
        """
        self.__dict__.update(json)
