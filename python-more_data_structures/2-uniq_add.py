#!/usr/bin/python3
def uniq_add(my_list=[]):
    s = 0
    newone = []
    for i in my_list:
        if i not in newone:
          newone.append(i)
          s = sum(newone)    
    return s
