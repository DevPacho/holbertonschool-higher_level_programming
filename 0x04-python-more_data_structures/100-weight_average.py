#!/usr/bin/python3
from curses import tparm
from pyrsistent import b


def weight_average(my_list=[]):
    if my_list:
        s = 0
        w = 0
        for tpl in my_list:
            a, b = tpl
            s += a * b
            w += b
        return s / w
