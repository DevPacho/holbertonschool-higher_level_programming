#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let element = 0; let count = 0;

  for (element of list) {
    if (element === searchElement) {
      count += 1;
    }
  } return count;
};
