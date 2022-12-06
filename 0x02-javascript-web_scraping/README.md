This is a README file for project 0x02. JavaScript - Web Scraping

There are 7 mandatory tasks in this project as follows:

Task 0 - Readme
 - Write a script that reads and prints the content of a file
  - The first argument is the file path
  - The content of the file must be read in UTF8
  - If an error occurred during the reading, print the error object

Task 1 - Write me
 - Write a script that writes a string to a file
  - The first argument is the file path
  - The second argument is the string to write
  - The content of the file must be written in UTF8
  - If an error occurred while writing, print the error object

Task 2 - Status code
 - Write a script that displays the status code of a GET reques
  - The first argument is the URL to request
  - The status code must be printed like this: code: <status code>
  - Must use the module request

Task 3 - Star Wars movie title
 - Write a script that prints the title of a StarWars movie where the episode
   number matches a given integer
  - The first argument is the movie ID
  - Must use the Star Wars API with the endpoint:
    https://swapi-api.hbtn.io/api/films/:id
  - Must use the module request

Task 4 - Star Wars Wedge Antilles
 - Write a script that prings the number of movies where the character "Wedge
   Antilles" is present
  - The furst argument is the API URL of the Star Wars API:
    https://swapi-api.hbtn.io/api/films/
  - Wedge Antilles is character ID 18. This script must use this ID for
    filtering the result of the API
  - Must use the module request

Task 5 - Loripsum
 - Write a script that gets the contets of a webpage and stores it in a file
  - The first argument is the URL to request
  - The second argument is the file path to store the body response
  - The file must be UTF8 encoded
  - Must use the module request

Task 6 - How many completed
 - Write a script that computes the number of tasks completed by user id
  - The first argument is the API URS:
    https://jsonplaceholder.typicode.com/todos
  - Only print users with completed task
  - Must use the module request
