#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
const squareSize = process.argv[2];
for (let i = 0; i < squareSize; i++) {
  process.stdout.write('X');
  for (let j = 1; j < squareSize; j++) {
    process.stdout.write('X');
  } process.stdout.write('\n');
}
