#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """The value is assigned for the size of the square"""
    def __init__(self, size=0):
        """'size' is an integer?"""
        if type(size) is int:
            """Private instance attribute 'size' with instantiation 'size'"""
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    """Public instance method that returns the current square area"""
    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size"""
        if type(value) is int:
            """Private instance attribute 'size' with instantiation 'size'"""
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    """Public instance method that prints the square with the character #"""
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print(self.__size * '#')
