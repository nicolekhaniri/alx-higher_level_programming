#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = []
    for i in set_1:
        for j in set_2:
            if i == j:
                set_3.append(i)
    return i
