#!/usr/bin/python3
def bigi_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        bigi = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > bigi:
                bigi = my_list[1]
    return(bigi)
