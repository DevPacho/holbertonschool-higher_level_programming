#!/usr/bin/python3
for a in reversed(range(97, 123)):
    if a % 2 == 0:
        a = chr(a)
    else:
        a = chr(a - 32)
    print(a, end="")
