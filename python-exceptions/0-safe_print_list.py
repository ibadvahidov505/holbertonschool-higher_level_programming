#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # end="" elementləri yan-yana yapışdırır
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            # Siyahı bitəndə dövrdən çıxırıq
            break
    # Bütün elementlərdən sonra bir dəfə yeni sətir
    print("")
    return count
