#!/usr/bin/python3
""" Module for empty BaseGeometry class
"""


class BaseGeometry:
    """ Empty class, except for exception
    """
    def area(self):
        raise Exception("area() is not implemented")
