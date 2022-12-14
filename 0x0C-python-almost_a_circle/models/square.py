#!/usr/bin/python3
"""
This module will inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class is specific to Squares
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instantiatize the Square class
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Override the __str__ method to return [Rectangle]
        (<id>) <x>/<y> - <size>
        """
        w = self.width
        x = self.x
        y = self.y
        iden = self.id
        return ("[Square] ({}) {}/{} - {}".format(iden, x, y, w))

    def update(self, *args, **kwargs):
        """
        Assigns a key:value argument to each attribute
        """
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.height = args[1]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.height = args[1]
                self.width = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.height = args[1]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]

        for key, value in kwargs.items():
            if key == "id":
                self.id = kwargs['id']
            if key == "size":
                self.height = kwargs['size']
                self.width = kwargs['size']
            if key == "x":
                self.x = kwargs['x']
            if key == "y":
                self.y = kwargs['y']

    @property
    def size(self):
        """
        Returns square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets square size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square
        """
        squareDict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return squareDict
