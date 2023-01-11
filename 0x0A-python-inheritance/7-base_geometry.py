#!/usr/bin/python3

"""Class BaseGeometry"""


class BaseGeometry:

    """
    The class has a function public instance method that raises an exception
    """

    def area(self):

        """
        Raise an Exception with a message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """
        Validates value
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
