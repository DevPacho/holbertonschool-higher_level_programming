#!/usr/bin/python3
"""class 'BaseGeometry'"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):

    """Constructor method"""
    def __init__(self, width, height):
        """Atributtes"""
        self.__width = width
        self.__height = height

        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """Area method"""
        return self.__width * self.__height

    def __str__(self):
        """Str method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
