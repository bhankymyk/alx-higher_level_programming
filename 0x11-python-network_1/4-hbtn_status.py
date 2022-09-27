#!/usr/bin/python3
"""
This Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    req = requests.get('https://intranet.hbtn.io/status')
    data = req.text
    data_type = type(data)

print("Body response:")
print("\t- type: {}".format(data_type))
print("\t- content: {}".format(data))
