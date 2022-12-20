#!/usr/bin/python3
class Square:
    """ defines the class square """
    def __init__(self, size=0):
        """ creates the private instance attribute size """
        """ initializes size as zero """
        if size != type(int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
