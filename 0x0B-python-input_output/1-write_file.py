#!/usr/bin/python3

"""Create a function to write in file"""

def write_file(filename="", text=""):
    """
    The file name and text is free to accept parameters
    Args:
        filename(str) The name of the file that will be written in
        text(str): The string of text that will be written in file
    Retrun:
        The number of characters added
    """
    with open(filename, w, encoding="utf-8") as file:
        num_char = file.write(text)
        return num_char
