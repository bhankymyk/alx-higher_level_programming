#!/usr/bin/node
const request = require('request');
request ('https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]),function (err, _res, body) {
        if (err) {
          console.log(err);
        }
        const info = JSON.parse(body);
        console.log(info.title);
      });
