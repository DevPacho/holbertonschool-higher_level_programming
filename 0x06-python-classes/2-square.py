#!/usr/bin/python3
"""Class that defines a square"""

class Square:
    """The value is assigned for the size of the square"""
    def __init__(self, size = 0):
        """'size' is an integer?"""
        if type(size) is int:
            """Private instance attribute 'size' with instantiation 'size'"""
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
