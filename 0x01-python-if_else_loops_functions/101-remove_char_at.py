#!/usr/bin/python3

def remove_char_at(str, n):
    i = 0
    temp = ""
    for c in str:
        if i != n:
            temp += c
    return (temp)
