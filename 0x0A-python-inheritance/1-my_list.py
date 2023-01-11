#!/usr/bin/python3
class MyList(list):
    """
    Class inherits from list
    """
    def print_sorted(self):
        """
        Prints the list and sorts in accending order
        """
        print(sorted(self))
