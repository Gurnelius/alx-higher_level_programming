#!/usr/bin/python3

for a in range(10):
    for b in range(10):
        if a == b or a > b:
            continue
        if (a < 9 and b < 9):
            print(f"{a}{b}, ", end='')
        elif a == 8 and b == 9:
            print(f"{a}{b}")
