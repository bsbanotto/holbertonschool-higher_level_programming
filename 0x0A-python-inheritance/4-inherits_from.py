#!/usr/bin/python3
""" This module checks to see if the object is an instance of a class that
inherited from the specified class
"""


def inherits_from(obj, a_class):
    """ This function returns True if object is an instance of a class
    that inherited from the specified class
    """
    if type(obj) == a_class:
        return False
    return True
