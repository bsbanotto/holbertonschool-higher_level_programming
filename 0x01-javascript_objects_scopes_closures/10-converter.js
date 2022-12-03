#!/usr/bin/node
exports.converter = function (base) {
  return function (numberObject) {
    return numberObject.toString(base);
  };
};
