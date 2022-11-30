#!/usr/bin/python3
for number in range(0, 100):
    if number >= 0 and number <= 9:
        print(f"{str(number).zfill(2)}, ", end="")
    elif number > 9 and number < 99:
        print(f"{number}, ", end="")
    else:
        print(f"{number}")
