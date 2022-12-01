#!/usr/bin/node
const args = process.argv.length;

// console.log(process.argv);
// console.log(args);
// console.log('number of args is '+args);

if (args === 2) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
