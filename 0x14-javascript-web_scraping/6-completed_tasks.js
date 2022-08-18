#!/usr/bin/node

const axios = require('axios');
const ApiURL = process.argv[2];

axios.get(ApiURL).then((response) => {
  const objData = {};

  for (const task of response.data) {
    if (task.completed === true) {
      if (!objData[task.userId]) {
        objData[task.userId] = 0;
      }
      objData[task.userId] += 1;
    }
  }
  console.log(objData);
});
