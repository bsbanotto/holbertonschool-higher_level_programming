#!/usr/bin/python3
""" Module for empty BaseGeometry class
"""


class BaseGeometry:
    """ Empty class, except for exception
    """
    def area(self):
        """ Function to raise exception that area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Function to validate value is of correct type
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
