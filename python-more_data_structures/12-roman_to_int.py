#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0

    nums = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    res = nums.get(roman_string[0], 0)

    for i in range(1, len(roman_string)):
        current = nums.get(roman_string[i], 0)
        prev = nums.get(roman_string[i - 1], 0)

        if current > prev:
            res += current - 2 * prev
        else:
            res += current

    return res
