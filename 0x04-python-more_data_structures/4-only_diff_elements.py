#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set(set_1):
        if i not in set(set_2):
            new_set.append(i)
    for i in set(set_2):
        if i not in set(set_1):
            new_set.append(i)
    return new_set
