#!/usr/bin/node
const SquareX = require('./5-square');

class Square extends SquareX {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let x = '';
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
      x = '';
    }
  }
}

module.exports = Square;
