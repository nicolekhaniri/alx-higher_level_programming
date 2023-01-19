#!/usr/bin/python3
import json

"""creating a class Base"""

class Base:

    """private class atribute"""

    __nb_objects = 0
    def __init__(self, id=None):
        
        """
        class constructor id is initialised to None
        """

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
            self.id = id
    @staticmethod
    """Returns list to dictionaries form json"""
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries is not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    """Saves json to dictionary to a file"""
    def save_to_file(cls, list_objs):
        new_dict = []
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        for items in list_objs:
            new_dict.append(items.to_dictionary())
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, "w") as f:
            f.write(json_string)
    @staticmethod
    """Returns the list of the json string representation"""
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)
    @classmethod
    """Returns an instance with all attributes already set"""
    def create(cls, **dictionary):
        pass
    @classmethod
    """Returns a list of instances"""
    def load_from_file(cls):
        pass
