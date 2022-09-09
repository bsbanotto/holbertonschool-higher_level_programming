#!/usr/bin/python3
"""Create a square with some safe guards to modify
the size and print square in # to stdout
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

    @property
    def size(self):
        """Retrieves the size of self
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of self square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square
        """
        return(self.__size * self.__size)

    def my_print(self):
        """Prints a square using # symbol to stdout
        """
        for i in range(0, self.__size):
            if i > 0:
                print()
            for j in range(0, self.__size):
                print("#", end="")
        print()
