#!/usr/bin/env python3
from calendar import c
from os import remove
import re


def no_c(my_string):
    remove = ""
    for a in my_string:
        if a not in 'cC':
            remove += a
    return remove
