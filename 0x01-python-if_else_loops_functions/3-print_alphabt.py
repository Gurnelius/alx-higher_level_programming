#!/usr/bin/python3

for letter in range(ord("a"), ord("z")+1):
    if chr(letter) in ('e', 'q'):
        continue
    print(chr(letter), end='')
