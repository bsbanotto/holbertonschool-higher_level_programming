#!/usr/bin/python3
def roman_to_int(roman_string):
    answer = 0
    give_or_take = 0
    if roman_string and type(roman_string) is str:
        roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                          'C': 100, 'D': 500, 'M': 1000}
        for numeral in range(len(roman_string) - 1, -1, -1):
            if roman_numerals[roman_string[numeral]] >= give_or_take:
                answer += roman_numerals[roman_string[numeral]]
            else:
                answer -= roman_numerals[roman_string[numeral]]
            give_or_take = roman_numerals[roman_string[numeral]]
        return answer

    else:
        return None
