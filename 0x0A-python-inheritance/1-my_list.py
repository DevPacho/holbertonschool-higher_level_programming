#!/usr/bin/python3
"""Class hat inherits from 'list'"""


class MyList(list):
    """Prints the list, but sorted (ascending sort)"""

    def print_sorted(self):
        print(sorted(self))
