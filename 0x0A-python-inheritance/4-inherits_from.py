#!/usr/bin/python3

"""Check if obj is an instance of a class inherited directly or indirectly"""


def inherits_from(obj, a_class):
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
