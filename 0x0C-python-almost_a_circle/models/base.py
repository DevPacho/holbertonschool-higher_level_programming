#!/usr/bin/python3
"""Base class"""

import json


class Base:
    """Class atributtes"""

    __nb_objects = 0

    """Class constructor"""
    def __init__(self, id=None):
        """Constructor method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of 'list_dictionaries'"""

        if list_dictionaries is None or not list_dictionaries or \
                list_dictionaries == " ":
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of 'list_objs' to a file"""

        save_list = []
        filename = f"{cls.__name__}.json"

        if list_objs is not None:
            for a in list_objs:
                save_list.append(cls.to_dictionary(a))

        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(save_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation 'json_string''"""

        list = []
        if json_string is None or not json_string or \
                json_string == " ":
            return list

        return json.loads(json_string)
