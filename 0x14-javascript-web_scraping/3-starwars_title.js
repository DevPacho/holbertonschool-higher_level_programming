#!/usr/bin/node

const axios = require('axios').default;
const Id = process.argv[2];
const IdURL = `https://swapi-api.hbtn.io/api/films/${Id}`

axios.get(IdURL).then(function (response) {
  console.log(response.data.title);
})
