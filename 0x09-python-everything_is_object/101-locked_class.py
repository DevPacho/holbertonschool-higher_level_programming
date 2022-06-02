#!/usr/bin/python3
"""
Class that prevents the user from dynamically creating
new instance attributes.
"""

class LockedClass:
    """if the new instance attribute is called 'first_name', don't prevents."""

    __slots__ = "first_name"
