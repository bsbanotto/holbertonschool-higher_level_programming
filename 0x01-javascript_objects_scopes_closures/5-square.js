#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = parseInt(w);
      this.height = parseInt(h);
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const placeHolder = this.width;
    this.width = this.height;
    this.height = placeHolder;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Rectangle;
module.exports = Square;
