#!/usr/bin/python3
"""Modules of a class student"""


class Student:

    def __init__(self, first_name, last_name, age):
        """Initiate a new student"""

    def to_json(self):
        """Get a dictionary representation of a Student"""
        return self.__dict__
