#!/usr/bin/node

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add (a, b) {
  const c = parseInt(a);
  const d = parseInt(b);

  if (isNaN(c) || isNaN(d)) {
    console.log('NaN');
  } else {
    console.log(c + d);
  }
}

add(arg1, arg2);
