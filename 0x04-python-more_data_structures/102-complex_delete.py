#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for index, a in list(a_dictionary.items()):
        if a == value:
            a_dictionary.pop(index)
    return a_dictionary
