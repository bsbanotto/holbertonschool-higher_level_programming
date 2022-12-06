#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(endpoint, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
