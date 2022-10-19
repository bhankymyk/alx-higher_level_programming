#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const completeTasks = {};
  for (const task of JSON.parse(body)) {
    if (task.complete === true) {
      if (task.userId in completeTasks) {
        completeTasks[task.userId] += 1;
      } else {
        completeTasks[task.userId] = 1;
      }
    }
  }
  console.log(completeTasks);
});
