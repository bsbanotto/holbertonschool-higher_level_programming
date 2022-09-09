#!/usr/bin/python3
"""This program divides every value in a matrix by a given divisor
"""


def matrix_divided(matrix, div):
    """matrix is the provided matrix, div is the divisor
    The matrix should consist only of ints or floats
    The divisor should also be an int or float, and not zero
    Resultant matrix should have values rounded to two places
    New matrix should be returned
    Each row of the matrix should be the same size
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div is None:
        raise TypeError("matrix_divided() missing 1\
                        required positional argument: 'div'")
    if type(div) is int:
        div = float(div)
    if type(div) is not float:
        raise TypeError("div must be a number")
    for row in range(0, len(matrix)):

        for num in range(0, len(matrix[row])):

            if type(num) is int:
                num = float(num)
            if type(num) is not float:
                raise TypeError("matrix must be a matrix \(list of lists)\
                                of integers/floats")

    return[[num/div for num in row] for row in matrix]
