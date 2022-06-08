#!/usr/bin/python3
"""Function that returns True if the object is exactly an instance
    of the specified class"""


def is_same_class(obj, a_class):
    """Is an instance verification"""

    if isinstance(obj, a_class):
        return True
    return False
