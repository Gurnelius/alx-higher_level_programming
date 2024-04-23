#!/usr/bin/node

const filesystem = require('fs');
const file = process.argv[2];
const content = process.argv[3];

filesystem.writeFile(file, content, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});