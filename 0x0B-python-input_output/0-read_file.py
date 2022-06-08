#!/usr/bin/python3
def read_file(filename=""):
    f = open("my_file_0.txt", "r")
    content = f.read()
    print(content)
    f.close()
