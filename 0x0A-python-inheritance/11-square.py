#!/usr/bin/python3
"""class 'BaseGeometry'"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Constructor method"""
    def __init__(self, size):
        self.__size = size

        super().integer_validator("size", size)

    def area(self):
        """Area method"""
        return self.__size ** 2

    def __str__(self):
        """Str method"""
        return "[Square] {}/{}".format(self.__size, self.__size)
