#!/usr/bin/python3
def uniq_add(my_list=[]):
    newone = []
    for i in my_list:
        if i not in newone:
            newone.append(i)
    return sum(newone)
