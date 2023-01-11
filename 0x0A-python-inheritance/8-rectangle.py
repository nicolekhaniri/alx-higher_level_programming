#!/usr/bin/python3
"""Inherits from base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""Class Rectangle"""


class Rectangle(BaseGeometry):

    """Defines class rectangle"""

    def __init__(self, width, height):

        """
        Initializes the rectangle
        """

        self.integer_validator("height", height)
        self.height = height
        self.integer_validator("width", width)
        self.width = width
