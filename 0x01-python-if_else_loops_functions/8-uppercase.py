#!/usr/bin/python3

def uppercase(str):
    upper = ""
    for c in str:
        if 'a' <= c <= 'z':
            upper += chr(ord(c)-ord('a')+ord('A'))
        else:
            upper += c

    print("{}".format(upper))
