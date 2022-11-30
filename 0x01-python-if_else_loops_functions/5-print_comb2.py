#!/usr/bin/python3
for number in range(0, 100):
    if number >= 0 and number <= 98:
        print("{:d}".format(number).zfill(2), end=", ")
    else:
        print("{:d}".format(number))
