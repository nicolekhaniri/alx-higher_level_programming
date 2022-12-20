#!/usr/bin/python3
"""area of a square """


class Square:
    """ define class Square """

    def __init__(self, size=0):
        """ creates private instance variable size
        Args: size - is initialized to size to 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
            """ size has to be an integer """
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate and return the area of the square"""
        return self.__size ** 2
