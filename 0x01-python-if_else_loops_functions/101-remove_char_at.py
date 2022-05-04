#!/usr/bin/python3
def remove_char_at(str, n):
    toremove = ""
    for a in range(len(str)):
        if a == n:
            toremove = toremove.replace(str[a], toremove)
            continue
        toremove = toremove + str[a]
    return(toremove)
