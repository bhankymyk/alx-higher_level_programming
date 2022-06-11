#!/usr/bin/python3
def big_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        big = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > big:
                big = my_list[1]
    return big
