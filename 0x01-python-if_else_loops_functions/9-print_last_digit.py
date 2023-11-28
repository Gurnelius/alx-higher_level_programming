#!/usr/bin/python

def print_last_digit(number):
    if number >= 0:
        digit = number % 10
    else:
        digit = number % -10 * -1

    print(f"{digit}", end='')
    return (digit)
