#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # Siyahıdan elementi götürürük və integer formatına salırıq
            # Əgər my_list[i] yoxdursa, burada IndexError yaranacaq və
            # funksiya (və proqram) məhz burada dayanacaq.
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Yalnız formatlama xətası olanda keçirik (skip)
            pass
    return count
