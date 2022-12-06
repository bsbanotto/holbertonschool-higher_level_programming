#!/usr/bin/node

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.appendFile(process.argv[3], body, function (writeError) {
      if (writeError) {
        console.log(writeError);
      }
    });
  }
});
