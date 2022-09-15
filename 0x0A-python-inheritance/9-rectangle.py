#!/usr/bin/python3
"""Module for rectangle class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is my Rectangle specific class
    """
    def __init__(self, width, height):
        """initializes my Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the self rectangle
        """
        return(self.__width * self.__height)

    def __str__(self):
        """Returns the human readable string representation of self
        """
        return("[Rectangle] {}/{}".format(self.__width, self.__height))
