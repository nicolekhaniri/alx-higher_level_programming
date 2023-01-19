#!/usr/bin/python3
from models.rectangle import Rectangle

"""create class square that inherits from rectangle"""

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        super().__init__(size)
        self.size = size
