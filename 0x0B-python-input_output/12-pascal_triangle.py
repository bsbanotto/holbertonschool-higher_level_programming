#!/usr/bin/python3
"""This module will print a Pascal's triangle
"""


def pascal_triangle(n):
    """This function will print a Pascal's triangle with 'n' rows
    """
    if n == 1:
        return[1]
    if n == 2:
        return[1, 1]
    if n > 2:
        triangle = []
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    value = triangle[i - 1][j - 1] + triangle[i -1][j]
                    row.append(value)
            triangle.append(row)

    return triangle
