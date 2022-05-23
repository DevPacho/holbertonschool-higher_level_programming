#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    to_increase = 0
    numbers = "0, 1, 2, 3, 4, 5, 6, 7, 8, 9"
    try:
        for traverse in range(x):
            if traverse in numbers:
                print(my_list[traverse], end="")
                to_increase += 1

    except Exception:
        pass
    print()
    return to_increase
