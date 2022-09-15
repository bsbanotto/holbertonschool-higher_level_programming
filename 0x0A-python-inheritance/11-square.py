#!/usr/bin/python3
"""Module for rectangle class that inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is my Rectangle specific class
    """
    def __init__(self, size):
        """initializes my Rectangle
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the self rectangle
        """
        return(self.__size * self.__size)

    def __str__(self):
        """Returns the human readable string representation of self
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
