#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    c = 0
    for c in range(len(str)):
        if c != n:
            new = new + str[c]
        return new
