#!/usr/bin/node
const numArray = [];
for (let i = 2; i < process.argv.length; i++) {
  numArray.push(parseInt(process.argv[i]));
}
// console.log(numArray);

if (numArray.length < 2) {
  console.log(0);
} else {
  let biggest = Number.MIN_VALUE;
  let secondBiggest = Number.MIN_VALUE;
  for (let i = 0; i < numArray.length; i++) {
    if (numArray[i] > biggest) {
      secondBiggest = biggest;
      biggest = numArray[i];
    } else if (numArray[i] > secondBiggest && numArray[i] !== biggest) {
      secondBiggest = numArray[i];
    }
  }
  console.log(secondBiggest);
}
