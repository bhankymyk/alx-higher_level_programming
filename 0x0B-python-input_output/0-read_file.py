#!/usr/bin/python3
"""It read a text file and print it to stdout"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
