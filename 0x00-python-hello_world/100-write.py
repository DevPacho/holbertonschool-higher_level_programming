#!/usr/bin/python3
from asyncore import write
import sys
str = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"

write(2, str, len(str))
exit(1)
