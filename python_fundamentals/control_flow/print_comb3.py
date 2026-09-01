#!/usr/bin/env python3
for x in range(0, 9):
    for y in range(x, 10):
        print(('{}{}\n' if x == 8 and y == 9 else '{}{}, ').format(x, y), end="")