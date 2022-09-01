#!/usr/bin/env python3
def no_c(my_string):
    newstring = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
        newstring += i
    return newstring
