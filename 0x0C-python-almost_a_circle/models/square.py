#!/usr/bin/python3
"""Class 'Square' that inherits from 'Rectangle'"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class constructor"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method with attributes"""
        super().__init__(size, size, x, y, id)

    """'size' getter and setter"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}" \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        args_len = len(args)

        if args:
            if args_len > 0:
                self.id = args[0]
            if args_len > 1:
                self.size = args[1]
            if args_len > 2:
                self.x = args[2]
            if args_len > 3:
                self.y = args[3]

        if args is None or args_len == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        return {"id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y}
