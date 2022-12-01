#!/usr/bin/node
const numLoops = parseInt(process.argv[2]);
if (process.argv.length <= 2) {
  console.log('Missing number of occurences');
} for (let i = 0; i < numLoops; i++) {
  console.log('C is fun');
}
