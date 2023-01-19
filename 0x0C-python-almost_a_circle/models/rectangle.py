#!/usr/bin/python3
from models.base import Base
import sys
"""creating class Rectangle"""

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """width"""
    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not type(int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """height"""
    @property
    def height(self):
        """
        height getter
        """
        return self.__height
    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not type(int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    """x"""
    @property
    def x(self):
        """
        x getter
        """
        return self.__x
    @x.setter
    def x(self, value):
        """
        x
        """
        if type(value) is not type(int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """y"""
    @property
    def y(self):
        """
        y getter
        """
        return self.__y
    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not type(int):
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.height * self.width

    def display(self):
        """
        Gives a visual representation of the Rectangle followed by a break
        """
        for i in range(self.y):
            print()
        for vertical in range(self.height):
            """traversing the height"""
            for j in range(self.x):
                """traversing the width"""
                print(" ", end="")
            for horizontal in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """overiding the __str__ method"""
        return (f"[Rectangle] {id} {x}/{y} - {width}/{height}")
    def update(self, *args, **kwargs):
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except BaseException:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
