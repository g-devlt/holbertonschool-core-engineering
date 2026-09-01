#!/usr/bin/env python3
print('{}'.format("".join([chr(x) for x in range(ord('a'), ord('z')+1) if chr(x) not in "eq"])), end="")
