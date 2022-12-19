#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    for i in range(x):
        try:
            if isinstance(i, int):
                print("{:d}".format(my_list[i]))
                length +=1
            else:
                continue
        except (ValueError, TypeError):
            continue
    return length
