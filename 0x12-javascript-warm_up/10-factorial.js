#!/usr/bin/node

const arg = process.argv[2];
const value = parseInt(arg);

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }
  if (n === 0) {
    return 0;
  }
  if (n === 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(value));
