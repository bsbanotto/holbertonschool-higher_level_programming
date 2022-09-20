#!/usr/bin/python3
"""
This module will inherit from Base
"""
from models.base import Base


class Rectangle(Base):
    """
    This class is specific to Rectangles
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiatize the Rectangle class
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Gets the width value
        """
        return self.__width

    @property
    def height(self):
        """
        Gets the height value
        """
        return self.__height

    @property
    def x(self):
        """
        Gets the x value
        """
        return self.__x

    @property
    def y(self):
        """
        Gets the y value
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Sets the width of self rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of self rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Sets the value of x offset
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Sets the value of y offset
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return(self.__height * self.__width)

    def display(self):
        """
        displays the rectangle using '#' symbols, offset by x and y
        """
        for line in range(0, self.__y):
            print("")
        for row in range(0, self.__height):
            for space in range(0, self.__x):
                print(" ", end="")
            for column in range(0, self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Override the __str__ method to return [Rectangle]
        (<id>) <x>/<y> - <width>/<height>
        """
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        iden = self.id
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(iden, x, y, w, h))

    def update(self, *args, **kwargs):
        """
        Assigns a key:value argument to each attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]

        for key, value in kwargs.items():
            if key == "id":
                self.id = kwargs['id']
            if key == "width":
                self.width = kwargs['width']
            if key == "height":
                self.height = kwargs['height']
            if key == "x":
                self.x = kwargs['x']
            if key == "y":
                self.y = kwargs['y']
