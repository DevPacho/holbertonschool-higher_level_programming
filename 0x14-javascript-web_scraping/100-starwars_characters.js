#!/usr/bin/node

const axios = require('axios');
const ID = process.argv[2];
const Movie = `https://swapi-api.hbtn.io/api/films/${ID}`;

axios.get(Movie).then((response) => {
  for (const people of response.data.characters) {
    axios.get(people).then((response) => {
      console.log(response.data.name);
    });
  }
});
