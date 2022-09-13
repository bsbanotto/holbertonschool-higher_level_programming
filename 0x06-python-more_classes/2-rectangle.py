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
        self.width = width
        self.height = height

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the area of self rectangle, or 0
        """
        area = self.__height * self.__width
        return(area)

    def perimeter(self):
        """ Returns the perimeter of self rectangle, or 0
        """
        if self.__height == 0 or self.__width == 0:
            return(0)
        return((self.__height + self.__width) * 2)

    def __str__(self):
        """ Loops through height and width to print a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return("")
        display = ""
        for i in range(0, self.__height):
            if i > 0:
                display += "\n"
            for j in range(0, self.__width):
                display += "#"
        return(display)
