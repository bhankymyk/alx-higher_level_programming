#!/usr/bin/python3
"""
This script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
