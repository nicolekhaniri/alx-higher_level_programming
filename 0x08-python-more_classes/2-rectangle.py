#!/usr/bin/python3
"""Defines class Rectangle"""
class Rectangle:
    def __init__(self, width=0, height=0):
        """height and width initialised to zero"""
        self. width = width
        self.height = height
    """
    width valuses
    """
    @property
    def width(self):
        """retrieve width"""
        return self.__width
    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif type(value) < 0:
            raise ValueError("width must be >= 0")
        else:
            return self.__width = value

    """
    height values
    """
    @property
    def height(self):
        """retrieves height"""
        return self.__width
    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif type(value) < 0:
            raise ValueError("height must be >= 0")
        else:
            return self.__height = value
    """
    public instance method that returns area of rectangle
    """
    def area(self):
        area = height * width
        return area
    """
    public instance method that returns perimeter of rectangle
    """
    def perimeter(self):
        if width = 0 or height = 0:
            return 0
        else:
            half = height + width
            peri = 2 * half
            return peri
