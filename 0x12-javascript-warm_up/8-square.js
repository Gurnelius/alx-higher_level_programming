#!/usr/bin/node
const arg = process.argv[2];
const value = parseInt(arg);
let x = '';

if (isNaN(value)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < value; i++) {
    for (let j = 0; j < value; j++) {
      x += 'X';
    }
    console.log(x);
    x = '';
  }
}
