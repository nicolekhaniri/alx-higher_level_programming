#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    last = (number[-1])
    last = int(last)
    number = int(last)
    print(f"{last}", end="")
    return last
