#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = list(set(my_list))
    for i in range(0, len(new_list)):
        sum += new_list[i]
    return sum
