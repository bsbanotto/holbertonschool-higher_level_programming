#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is my Square specific class
    """
    def __init__(self, size):
        """initializes my Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of the self Square
        """
        return(self.__size * self.__size)

    def __str__(self):
        """Returns the human readable string representation of self
        Now it says [Square]
        """
        return("[Square] {}/{}".format(self.__size, self.__size))
