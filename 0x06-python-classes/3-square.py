#!/usr/bin/python3
class Square:
    """ define class Square """
    def __init__(self, size = 0):
        """ creates private instance variable size """
        """ initializes size to 0 """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """ size has to be an integer """
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        return self.__size ** 2
