#!/usr/bin/node
exports.converter = function (base) {
  return toString(base);
};

/*
I know that if I do numberObject.toString(base) I'll get the correct answer
I don't know how to get number where I need it
https://stackoverflow.com/questions/1337419/how-do-you-convert-numbers-between-different-bases-in-javascript
Test file:
myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));

In the above, 16 is base. That's easy to get, it's directly passed
in the console.log(myConverter(numberObject))
How do I get that infront of my toString(base);
*/

/* This code works
How the hell does `return function (numberObject)` get the integer from myConverter???????
exports.converter = function (base) {
  return function (numberObject) {
    return numberObject.toString(base)
  }
};
*/
