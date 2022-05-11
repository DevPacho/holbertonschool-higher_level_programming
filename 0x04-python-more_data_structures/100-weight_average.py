#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        s = 0
        w = 0
        for tpl in my_list:
            a, b = tpl
            s += a * b
            w += b
        return s / w
    return 0
