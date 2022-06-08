#!/usr/bin/python3
"""class 'BaseGeometry'"""


class BaseGeometry:
    """Area method"""
    def area(self):
        """Error handling method"""
        raise Exception("area() is not implemented")

    """Value validation"""
    def integer_validator(self, name, value):
        """Validations of type and value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
