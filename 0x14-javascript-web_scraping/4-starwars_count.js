#!/usr/bin/node

const axios = require('axios');
const ApiURL = process.argv[2];

axios.get(ApiURL).then((response) => {
  const obj = 'https://swapi-api.hbtn.io/api/people/18/';
  axios.get(obj).then((response2) => {
    console.log(response2.data.films.length);
  });
});
