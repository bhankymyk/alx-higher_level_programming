#!/usr/bin/python3
for num in range(0, 10):
    for nums in range(num + 1, 10):
        if num == 8 and nums == 9:
            print("{}{}".format(num, nums))
        else:
            print("{}{}".format(num, nums), end=", ")
