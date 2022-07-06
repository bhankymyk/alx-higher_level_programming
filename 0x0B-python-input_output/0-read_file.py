#!/usr/bin/python3
"""It read a text file and print it to stdout"""


def read_file(filename=""):
    """print the content of a UTF-8 into stdout"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
