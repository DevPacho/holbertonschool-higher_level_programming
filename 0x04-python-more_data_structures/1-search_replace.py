#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for index, a in enumerate(new_list):
        if a == search:
            my_list[index] = replace
    return new_list
