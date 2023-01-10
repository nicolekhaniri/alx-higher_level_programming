#!/usr/bin/python3

"""Creates class Student"""
class Student:
    """
    Public Attributes for student.
    Public Methods:
        to_json: retrieves dictionary representation
    """
    def __init__(self, first_name, last_name, age):
        first_name = self.first_name
        last_name = self.last_name
        age = self.age
    def to_json(self):
        return self.__dict__
