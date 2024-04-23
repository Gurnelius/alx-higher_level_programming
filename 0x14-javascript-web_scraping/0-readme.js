#!/usr/bin/node

const filesystem = require('fs');
const file = process.argv[2];

filesystem.readFile(file, 'utf-8', (error, content) => {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});