#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    """
    if not a_dictionary:
        return None

    # max(dictionary) normalda açarları (key) əlifba sırası ilə müqayisə edir.
    # Amma key=a_dictionary.get əlavə etdikdə, o, açarları DEYERLERE görə müqayisə edir.
    return max(a_dictionary, key=a_dictionary.get)
