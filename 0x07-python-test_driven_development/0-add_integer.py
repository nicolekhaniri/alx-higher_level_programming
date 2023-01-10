#!/usr/bin/python3
"""Function that adds to integers """

def add_integer(a, b=98):
    """ Adds two integers a and b 
    """
    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
