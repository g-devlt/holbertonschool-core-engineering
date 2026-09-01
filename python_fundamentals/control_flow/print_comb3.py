#!/usr/bin/env python3
for x in range(0, 9):
    for y in range(x+1, 10):
        s = '{}{}\n' if x == 8 and y == 9 else '{}{}, '
        print(s.format(x, y), end="")
