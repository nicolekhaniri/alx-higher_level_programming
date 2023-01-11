#!/usr/bin/python3

"""Check if obj is an instance of a_class"""


def is_same_class(obj, a_class):

    """
    Return:
        True if yes and False if no
    """
    if isinstance(obj, a_class):
        return True
    else:
        retrun False
