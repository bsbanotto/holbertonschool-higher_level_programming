#!/usr/bin/python3
"""This module creates a square with no safety net
"""


class Square:
    """This class defines a square based on size
    Size is the length of any one side
    Size will be a private attribute
    """
    def __init__(self, size=0):
        """This method initializes the square
        """
        self.__size = size
