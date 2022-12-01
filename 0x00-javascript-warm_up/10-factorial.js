#!/usr/bin/node
const number = parseInt(process.argv[2]);

function factorial (number) {
  if (number === 0) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}

if (isNaN(number)) {
  console.log(1);
} else {
  console.log(factorial(number));
}
