#!/usr/bin/python3

"""Checks if object is an instance of a class inherited from specifies class"""


def is_kind_of_class(obj, a_class):
    """
    Return: 
        True if yes and False if no
    """
    return isinstance(obj, a_class)
