#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Əgər element integer deyilsə, sadəcə keçirik
            continue
        except IndexError:
            # Siyahı bitibsə, dövrü tamamilə dayandırırıq
            break
    print("")  # Sonda yeni sətir
    return count
