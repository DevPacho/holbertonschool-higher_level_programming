#!/usr/bin/node

exports.esrever = function (list) {
  const ReversedList = [];

  for (let element = list.length - 1; element >= 0; element--) {
    ReversedList.push(list[element]);
  } return ReversedList;
};
