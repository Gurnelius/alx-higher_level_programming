#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    members = dir(hidden_4)
    sorted(members)
    for m in members:
        if m.startswith("__"):
            continue
        print(m)
