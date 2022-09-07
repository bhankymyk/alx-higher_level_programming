#!/usr/bin/node
module.exports = class Square extends requestAnimationFrame('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }
};
