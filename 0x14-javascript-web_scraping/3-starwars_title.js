#!/usr/bin/node
const request = require('request');
request ('https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]),function (err, response, body) {
        if (err) {
          console.log(err);
        }
        console.log(JSON.parse(body).title);
      });
