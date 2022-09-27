#!/usr/bin/python3
"""
This Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.
"""

import email
import sys
import requests
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    url_param = {'email': email}

    req = requests.post(url, data=url_param)
    print(req.text)
