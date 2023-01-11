#!/usr/bin/python3

"""Check if obj is an instance of a class inherited directly or indirectly"""


def inherits_from(obj, a_class):
    if issubclass(obj, a_class) or isinstance(obj, a_class):
        return True
    else:
        return False
