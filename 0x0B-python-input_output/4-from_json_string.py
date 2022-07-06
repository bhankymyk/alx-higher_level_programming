#!/usr/bin/python3
"""Python representation of a json"""
import json


def from_json_string(my_str):
    """Convert json string to python object"""
    return json.loads(my_str)
