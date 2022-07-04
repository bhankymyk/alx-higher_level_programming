#!/usr/bin/python3
"""This module inherit from list"""


class MyList(list):

    def print_sorted(self):
        """print the list, but sorted"""
        print(sorted(self))
