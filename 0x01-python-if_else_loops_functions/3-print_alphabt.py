#!/usr/bin/python3
for char in range(97, 123):
    if char != 'q' and char != 'e':
        print("{}".format(char + ord("a")), end="")
