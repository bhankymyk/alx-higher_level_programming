#!/usr/bin/python3

import sys

if (__name__ == "__main__"):
    i = 1
    result = 0
    arguments = len(sys.argv) - 1

    if (arguments != 0):
        while (i <= arguments):
            result += int(sys.argv[i])
            i += 1
            print(result)
