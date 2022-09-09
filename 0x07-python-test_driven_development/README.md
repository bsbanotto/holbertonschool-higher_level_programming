This is a README for 0x07-Python - Test-driven development

There are 6 mandatory tasks in this project

Task 0 - Integers addition
 - Write a function that adds 2 integers:
    - Prototype: def add_integer(a, b=98)
    - a and b must be integers or floats, otherwise raise TypeError exception
    - a and b must be typecasted to integers if they are floats
    - Returns an integer 

Task 1 - Divide a matrix
 - Write a function that divides all elements of a matrix
    - Prototype: def matrix_divided(matrix, div)
    - matrix must be a list of lists of integers or floats, otherwise raise TypeError exception
    - Each row of the matrix must be the same size, otherwise raise TypeError exception
    - div must be a number, otherwise raise TypeError exception
    - Div can't be equal to zero, otherwise raise a ZeroDivisionError exception
    - All elements of the matrix shoule be divided by div, rounded to 2 decimal places
    - Return a new matrix

Task 2 - Say my name
 - Write a function that prints "My name is <first name> <last name>
    - Prototype: def say_my_name(first_name, last_name="")
    - first_name and last_name must be strings, otherwise raise TypeError exception

Task 3 - Print Square
 - Write a function that prints a square with the character #
    - Prototype def print_square(size)
    - size is the length of a side of the square
    - Size must be an integer, otherwise raise TypeError exception
    - If size is less than 0, raise ValueError exception
    - If size is a float and is less than 0, raise a TypeError exception

Task 4 - Text indentation
 - Write a function that prints a text with 2 new lines after each of these characters: ., ?, :
    - Prototype def text_indentation(text)
    - text must be a string, otherwise raise a TypeError exception
    - There should be no space at the beginning or at the end of each printed line

Task 5 - Max integer - Unittest
 - Write unittests for the function def max_integer(list=[])
    - Test file should be inside a folder tests
    - Must use the unittest module
    - Test file should be python extension
    - Test file should be executed by the command:
      python3 -m unittest test.6-max_integer_test
    - All test must be passable by the give function
