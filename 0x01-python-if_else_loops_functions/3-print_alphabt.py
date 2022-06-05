#!/usr/bin/python3
for char in range(97, 123):
    if char != 4 and char != 16:
        print("{}".format(char + ord("a")), end="")
