#!/bin/bash
#This  script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sl "$1" | grep 'Content-Length:' | cut -d ' ' -f2
