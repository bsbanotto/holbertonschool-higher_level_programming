This is a README file for project 0x01. JavaScript - Objects, Scopes and
Closures

There are 11 mandatory tasks in this project as follows:

Task 0 - Rectangle #0
 - Write an empty class `Rectangle` that defines a rectangle
  - Must use the `class` notation for defining the class

Task 1 - Rectangle #1
 - Write a class `Rectangle` that defines a rectangle
  - Must use the `class` notation for defining the class
  - The constructor must take 2 arguments, w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h

Task 2 - Rectangle #2
 - Write a class `Rectangle` that defines a rectangle
  - Must use the `class` notation for defining the class
  - The constructor must take 2 arguments, w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0, or not a positive integer, create an empty object

Task 3 - Rectangle #3
 - Write a class `Rectangle` that defines a rectangle
  - Must use the `class` notation for defining the class
  - The constructor must take 2 arguments, w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0, or not a positive integer, create an empty object
  - Create an instance method called print() that prints the rectangle using
    the character x

Task 4 - Rectangle #4
 - Write a class `Rectangle` that defines a rectangle
  - Must use the `class` notation for defining the class
  - The constructor must take 2 arguments, w and h
  - Initialize the instance attribute width with the value of w
  - Initialize the instance attribute height with the value of h
  - If w or h is equal to 0, or not a positive integer, create an empty object
  - Create an instance method called print() that prints the rectangle using
    the character x
  - Create an instance method called rotate() that exchanges the width and
    height of the rectangle
  - Create an instance method called double() that multiplies the width and
    height of the rectangle by 2

Task 5 - Square #0
 - Write a class `Square` that defines a square and inherits from `Rectangle`
   of 4-rectangle.js
  - Must use the `class` notation for defining the class and extends
  - The constructor must take 1 argument, size
  - The constructor of Rectangle must be callued bu using super()

Task 6 - Square #1
 - Write a class `Square` that defines a square and inherits from `Rectangle`
   of 4-rectangle.js
  - Must use the `class` notation for defining the class and extends
  - Create an instance method called charPrint(c) that prints the rectangle
    using the character 'c'
        - If 'c' is undefined, use the character 'X'

Task 7 - Occurrences
 - Write a function that returns the number of occurrences in a list
  - Prototype: exports.nboccurences = function (list, searchElement)

Task 8 - Esrever
 - Write a function that returns the reversed version of a list
  - Prototype: experts.esrever = function (list)
  - Not allowed to use the built-in mnethod reverse

Task 9 - Log me
 - Write a function that prints the number of arguments already printed and
   the new argument value (see example below)
  - Prototype: exports.logMe = function (item)
  - Output format: <number arguments already printed>: <current argument value>

  Example:
    $ cat 9-main.js
    #!/usr/bin/node
    const logMe = require('./9-logme').logMe;

    logMe("Hello");
    logMe("Best");
    logMe("School");

    $ ./9-main.js
    0: Hello
    1: Best
    2: School

Task 10 - Number conversion
 - Write a function that converts a number from base 10 to another base passed
   as an argument
  - Prototype: exports.converter = function (base)
  - Not allowed to import any file
  - Not allowed to declare any new variable
