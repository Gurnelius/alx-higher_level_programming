#!/usr/bin/node
const arg = process.argv[2];
const numberValue = parseInt(arg);

if (!isNaN(numberValue)) {
  console.log('My number:', numberValue);
} else {
  console.log('Not a number');
}
