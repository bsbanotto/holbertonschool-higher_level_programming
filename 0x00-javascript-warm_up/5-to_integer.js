#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else if (process.argv.length < 3) {
  console.log('Not a number');
} else {
  console.log('My numner: ' + parseInt(process.argv[2]));
}
