#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    difr = []
    for i in set_1:
        if i not in set_2:
            difr.append(i)
    for k in set_2:
        if k not in set_1:
            difr.append(k)
    return difr
