#!/usr/bin/python3
from models.base import Base
from models.rectangle import Rectangle

"""create class square that inherits from rectangle"""

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        height = width
        size = height
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        super().__init__(size)
        self.size = size
    def __str__(self):
        return (f"[Square] {id} {x}/{y} - {size}")
    """
    square getter and setter for size
    """
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        self.__size = value
    
    """
    args and kwargs
    """
    def update(self, *args, **kwargs):
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except BaseException:
                pass
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
    def to_dictionary(self):
        dict(my_dict) = {'id': self.id,'size': self.size,'x': self.x,'y': self.y}
        return my_dict
