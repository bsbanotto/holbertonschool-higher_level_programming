#!/usr/bin/node
exports.converter = function (base) {
  return number.toString(base);
};
// I know that if I do number.toString(base) I'll get the correct answer
// I don't know how to get number where I need it
// Test file:
// myConverter = converter(16);

// console.log(myConverter(2));
// console.log(myConverter(12));
// console.log(myConverter(89));

// In the above, 16 is base. That's easy to get
// in the console.log(myConverter(number))
// How do I get that number infront of my toString(base);
