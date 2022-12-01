This is a README for project 0x00. JavaScript - Warm up

There are 14 mandatory tasks in this project as follows:

Task 0 - First constant, first print
 - Write a script that prints "JavaScript is amazing":
  - Must create a constant variable called myVar
   - myVar value is "JavaScript is amazint"
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 1 - 3 Languages
 - Write a script that prints 3 lines:
  - The first line: "C is fun"
  - The second line: "Python is cool"
  - The third line: "JavaScript is amazing"
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 2 - Arguments
 - Write a script that prints a message depending on the number of arguments
  - If no argument: "No argument"
  - If only one argument: "Argument found"
  - Otherwise: "Arguments found"
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 3 - Value of my argument
 - Write a script that prints the first argument passed to it
  - If no argument: "No argument"
  - Must use console.log(...) to print all output
  - Not allowed to use var
  - Not allowed to use length

Task 4 - Create a sentence
 - Write a script that prints two arguments passed to it separated by is
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 5 - An Integer
 - Write a script that prints My number: <first arg converted to int>
  - IF the first argument can be converted to an integer
 - If the argument can't be converted: "Not a number"
 - Must use console.log(...) to print all output
 - Not allowed to use var
 - Not allowed to use try/catch

Task 6 - Loop to languages
 - Write a script that prints 3 lines, using an array of string and a loop
  - The first line: "C is fun"
  - The second line: "Python is cool"
  - The third line: "JavaScript is amazing"
  - Must use console.log(...) to print all output
  - Not allowed to use var
  - Not allowed to use any if/else statement
  - Can only use one console.log
  - Must use a loop

Task 7 - I love C
 - Write a script that prints x times "C is fun"
  - Where x is the first argument of the script
  - If the first argument can't be converted to an integer
   - print: "Missing number of occurrences"
  - Must use console.log(...) to print all output
  - Not allowed to use var
  - Can only use one console.log
  - Must use a loop

Task 8 - Square
 - Write a script that prints a square
  - The first argument is the size of the square
  - If the first argument can't be converted to an integer
   - print: "Missing size"
  - Must use console.log(...) to print all output
  - Not allowed to use var
  - Must use a loop

Task 9 - Add
 - Write a script that prints the addition of 2 integers
  - First argument is first integer
  - Second argument is second integer
  - Function prototype: `function add(a, b)`
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 10 - Factorial
 - Write a script that computes and prints a factorial
  - First argument is an integer
  - Factorial of NaN is 1
  - Must do it recursively
  - Must use a function
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 11 - Second biggest!
 - Write a script that searches for the second biggest integer in a list
  - Can assume all arguments can be converted on integer
  - If one or none arguments, print: 0
  - Must use console.log(...) to print all output
  - Not allowed to use var

Task 12 - Object
 - Update given script to replace the value 12 with 89
 - Not allowed to use var

        guillaume@ubuntu:~/0x12$ cat 12-object.js
        #!/usr/bin/node
        const myObject = {
        type: 'object',
        value: 12
        };
        console.log(myObject);
        /*
        YOUR CODE HERE
        */
        console.log(myObject);

        guillaume@ubuntu:~/0x12$ ./12-object.js
        { type: 'object', value: 12 }
        { type: 'object', value: 89 }
        guillaume@ubuntu:~/0x12$ 

Task 13 - Add file
 - Write a function that returns the addition of 2 integers
  - The function must be visible from outside
  - The name of the funciton must be add
  - Not allowed to use var
