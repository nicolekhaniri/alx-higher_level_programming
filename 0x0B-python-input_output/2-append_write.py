#!/usr/bin/python3

"""Creates a function to append text to the file"""


def append_write(filename="", text=""):
    """
    filename and text is free to accept parameters

    Args:
        filename(str): The name of the file to append to
        text(str): The string of text to append to the file
    Return:
        The number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as new:
        num_char = new.write(text)
        return num_char
