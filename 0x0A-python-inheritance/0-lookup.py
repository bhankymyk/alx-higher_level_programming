#!/usr/bin/python3
"""Module that returns the list of available
 attributes and methods of an object"""


def lookup(obj):
    """it returns the list of attributes and methods of obj"""

    return(dir(obj))
