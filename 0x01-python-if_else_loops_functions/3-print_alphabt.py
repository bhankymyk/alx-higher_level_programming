#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) != 4 and chr(letter) != 16:
        print("{}".format(chr(letter)), end="")
