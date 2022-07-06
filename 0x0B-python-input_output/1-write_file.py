#!/usr/bin/python3
"""This module writes a string to a text file
 (UTF8) and returns the number of characters"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
