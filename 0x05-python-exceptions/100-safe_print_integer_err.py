#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if value < 0 or value >= 0:
            print("{:d}".format(value))
            return True
    except Exception as ex:
        sys.stderr.write("Exception: {}\n".format(ex))
        return False
    else:
        print("{:s} is not an integer".format(value))
