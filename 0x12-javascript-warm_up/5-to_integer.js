#!/usr/bin/node
arg = parseInt(process.argv[2]);

if (arg === undefined) {
  console.log('Not a number');
} else {
  console.log(arg);
}
