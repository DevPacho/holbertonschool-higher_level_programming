#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cpy = my_list.copy()
    for a in cpy:
        if a % 2 == 0:
            cpy[a] = True
        else:
            cpy[a] = False
        a += 1
    return cpy
