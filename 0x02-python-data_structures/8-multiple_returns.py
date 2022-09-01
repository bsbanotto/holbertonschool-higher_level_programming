#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        length = 0
    else:
        length = len(sentence)
#    print(length)

    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
#    print(first)

    ret_pair = length, first
    return ret_pair
