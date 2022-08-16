#!/usr/bin/node

exports.callMeMoby = function (times, funct) {
  for (let repeat = 0; repeat < times; repeat++) {
    funct()
  }
}
