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
    def to_json_string(list_dictionaries):
        """
        Returns list to dictionaries from json
        """
        if list_dictionaries is None or list_dictionaries is not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves json to dictionary to a file
        """
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
    def from_json_string(json_string):
         """
         Returns the list of the json string representation
         """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        """
        pass
    @classmethod
    def load_from_file(cls):
         """
         Returns a list of instances
         """
        pass
