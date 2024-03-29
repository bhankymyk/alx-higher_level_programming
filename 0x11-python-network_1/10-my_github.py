#!/usr/bin/python3
"""
This script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id 
"""

from sys import argv
import requests

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]

    try:

        req =  requests.get('https://api.github.com/user', auth=(
            argv[1], argv[2])).json()
        print(req.get('id'))
    except:
        print("None")
