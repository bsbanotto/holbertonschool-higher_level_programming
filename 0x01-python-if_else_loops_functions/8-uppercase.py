#!/usr/bin/python3
def uppercase(str):
    uppercasestring = ""
    for i in str:
        if ord(i) in range(97, 123):
            uppercasestring += chr(ord(i) - 32)
        else:
            uppercasestring += chr(ord(i))
    print(uppercasestring)
