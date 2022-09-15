#!/usr/bin/python3
""" This will return a list of available attributes and methods
of an object
"""


def lookup(obj):
    """ This lookup method does all of the work
    """
    return dir(obj)
