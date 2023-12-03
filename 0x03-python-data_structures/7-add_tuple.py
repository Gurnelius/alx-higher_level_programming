#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    diff = len(tuple_a) - len(tuple_b)
    if diff < 0:
        for i in range(abs(diff)):
            tuple_a = tuple_a + (0,)
    elif diff > 0:
        for i in range(abs(diff)):
            tuple_b = tuple_b + (0,)
    result_tuple = tuple(x + y for x, y in zip(tuple_a, tuple_b))

    return result_tuple
