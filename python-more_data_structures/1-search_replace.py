#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list=[]
    for i in my_list:
        if i==2:
            i=89
            new_list.append(i)
        else:
            new_list.append(i)
    print(new_list)
    print(my_list)
my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)
