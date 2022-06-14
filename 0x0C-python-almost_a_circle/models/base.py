#!/usr/bin/python3
"""Base class"""


class Base:
    """Class atributtes"""

    __nb_objects = 0

    """Class constructor"""
    def __init__(self, id=None):
        """Constructor method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
