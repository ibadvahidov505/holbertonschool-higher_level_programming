#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newone = []
    for i in range(list_length):
        res = 0  # Hər addımda nəticəni əvvəlcə 0 təyin edirik
        try:
            # Bölməni yerinə yetirməyə çalışırıq
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            # Xəta olsa da, olmasa da nəticəni (ya bölməni, ya 0-ı) əlavə edirik
            newone.append(res)
    return newone
