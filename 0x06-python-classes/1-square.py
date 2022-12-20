#!/usr/bin/python3
""" defines a square """


class Square:
    """ class Square to define a square based on 0-square.py """
    """ size is a private attribute """
    def __init__(self, size=0):
        """ size is initialized as zero
        Args: size - represents the size of the square
        """
        self.__size = size
