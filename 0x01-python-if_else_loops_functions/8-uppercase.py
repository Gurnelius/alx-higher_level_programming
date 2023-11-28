#!/usr/bin/python3

def uppercase(str):
    for c in str:
        print(chr(ord(c)-ord('a')+ord('A')) if 'a' <= c <= 'z' else c, end='')
    print("\n", end='')
