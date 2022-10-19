#!/usr/bin/node
const request = require('request');
request ({
    starWarsurl: 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]),
    json: true
    }, 
  function (error, _res, body) {
    if (error) {
      console.log(error);
    }
    console.log(body.title);
  });
