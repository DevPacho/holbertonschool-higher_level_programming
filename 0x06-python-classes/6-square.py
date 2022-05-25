#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Constructor method that initialize and create a 'square' object"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """Public instance method that returns the current square area"""
    def area(self):
        return self.__size ** 2

    """Getter for size"""
    @property
    def size(self):
        """Retrieve the size"""
        return self.__size

    """Setter for size"""
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

        print(self.__position[1] * '\n', end="")
        for traverse in range(self.__size):
            print(self.__position[0] * " " + self.__size * '#')

    """Getter for position"""
    @property
    def position(self):
        """Retrieve the position"""
        return self.__position

    """Setter for position"""
    @position.setter
    def position(self, value):
        """Set the position"""
        if type(value) is tuple or len(value) == 2 or type(value[0]) is int \
                or type(value[1]) is int or value[0] > 0 or value[1] > 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
