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

    def to_json(self):
        """Send Student to JSON
        """
        return vars(self)
