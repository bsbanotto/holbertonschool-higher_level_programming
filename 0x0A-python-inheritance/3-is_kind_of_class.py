#!/usr/bin/python3
""" This module checks to see if an object is an instance of, or instance of a class
that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """ Returns true if obj is an instance or inherited from spec'd class
    """
    return isinstance(obj, a_class)
