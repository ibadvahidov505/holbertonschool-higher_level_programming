#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    newones = {key: value}
    a_dictionary.update(newones)
    return a_dictionary
