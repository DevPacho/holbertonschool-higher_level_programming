#!/usr/bin/python3
"""Class that inherits from int"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""

    def __eq__(self, input):
        """To get called on comparison using == operator."""
        return int.__eq__(self, input)

    def __ne__(self, input):
        """To get called on comparison using != operator."""
        return int.__ne__(self, input)
