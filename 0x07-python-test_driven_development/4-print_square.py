#!/usr/bin/python3
"""This program prints a square using the # symbol at a give size
"""


def print_square(size):
    """This function prints the square with error handling
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("ize must be an integer")

    for i in range(0, size):
        print("#" * size)
