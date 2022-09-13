#!/usr/bin/python3
""" This module will define a rectangle by width and height
TypeError will be raised if width and height are not integers
ValueError will be raised if width and height are less than 0
width and height are private attributes
"""


class Rectangle:
    """ Rectangle definitions will take place here
    """
    def __init__(self, width=0, height=0):
        """ Here is the metod to initialize our rectangle
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """ Retrieves the width of self
        """
        return self.__width

    @property
    def height(self):
        """ Retrieves the height of self
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ Sets the width of self rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ Sets the height of self rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
