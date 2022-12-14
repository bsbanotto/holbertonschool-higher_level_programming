#!/usr/bin/python3
"""Create a square with some safe guards
"""


class Square:
    """Class to define a square
    """
    def __init__(self, size=0):
        """This method initializes the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
