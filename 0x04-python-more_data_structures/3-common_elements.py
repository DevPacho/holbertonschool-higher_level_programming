#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_a = set(set_1)
    set_b = set(set_2)

    return list(set(set_a).intersection(set_b))
