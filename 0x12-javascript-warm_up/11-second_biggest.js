#!/usr/bin/node

function NumericSort (n1, n2) {
  return n1 - n2;
}

const process = require('process');
const argsSlice = process.argv.slice(2);
const len = argsSlice.length;
let number = 0;

if (len > 1) {
  argsSlice.sort(NumericSort);
  number = argsSlice[len - 2];
} console.log(number);
