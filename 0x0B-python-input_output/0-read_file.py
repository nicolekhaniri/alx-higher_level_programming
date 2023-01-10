#!/usr/bin/python3

"""Create the function to read file"""

def read_file(filename=""):
    """
    Args:
        filename(str): The name of the file that will be read
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read())
