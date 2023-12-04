#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result_tuple = []
    for i in range(2):
        try:
            a = tuple_a[i]
        except:
            a = 0
        try:
            b = tuple_b[i]
        except:
            b = 0
        result_tuple.append(a + b)
    return tuple(result_tuple)
