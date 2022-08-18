#!/usr/bin/node

const axios = require('axios');
const ApiURL = process.argv[2];

axios.get(ApiURL).then((response) => {
  let times = 0;

  for (const ID of response.data.results) {
    for (const person of ID.characters) {
      if (person.includes('18')) {
        times++;
      }
    }
  }
  console.log(times);
});
