#!/usr/bin/python3
""" This module checks to see if an object is in the same class
"""


def is_same_class(obj, a_class):
    """ Returns true if obj is an instance of the class
    """
    return type(obj) == a_class
