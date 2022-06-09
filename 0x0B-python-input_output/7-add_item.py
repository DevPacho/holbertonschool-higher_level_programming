#!/usr/bin/python3
"""Script that adds all arguments to a Python list,
    and then save them to a file"""

import json
from sys import argv
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_exists = exists("add_items.json")
file = "add_items.json"
list = []

if (file_exists):
    list = load_from_json_file("add_items.json")
    for args in argv[1:]:
        list.append(args)
else:
    list = []

save_to_json_file(list, "add_items.json")
