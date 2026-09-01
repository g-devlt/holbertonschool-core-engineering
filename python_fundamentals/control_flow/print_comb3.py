#!/usr/bin/env python3
for x in range(0, 10):
    for y in range(x, 10):
        print(('{}{}, ' if x == 9 and y == 9 else '{}{}').format(x, y))