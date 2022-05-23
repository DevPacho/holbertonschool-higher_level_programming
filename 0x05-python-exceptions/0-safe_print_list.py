#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    to_increase = 0
    try:
        for traverse in range(x):
            print(my_list[traverse], end="")
            to_increase += 1

    except IndexError:
        pass
    print()
    return to_increase
