#!/usr/bin/node
const arg = process.argv[2];
const value = parseInt(arg);

if (isNaN(value)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
}
