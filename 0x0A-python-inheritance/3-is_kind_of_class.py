#!/usr/bin/python3

"""Checks if object is an instance of a class inherited from specifies class"""


def is_kind_of_class(obj, a_class):
    """
    Return: 
        True if yes and False if no
    """
    if isinstance(obj, a_class) or issubclass(obj, a_class):
        return True
    else:
        return False
