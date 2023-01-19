#!/usr/bin/python3

"""creating a class Base"""

class Base:

    """private class atribute"""

    __nb_objects = 0
    def __init__(self, id=None):
        
        """
        class constructor id is initialised to None
        """

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
            self.id = id
