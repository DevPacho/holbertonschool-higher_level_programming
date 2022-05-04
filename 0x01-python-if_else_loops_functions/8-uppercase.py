#!/usr/bin/python3
def uppercase(str):
    for a in range(len(str)):
        if (ord(str[a]) >= 97 and ord(str[a]) <= 122):
            str[a] = ord(str[a]) - 32
            str[a] = chr(str[a])
        print(str[a], end="")
    print()
