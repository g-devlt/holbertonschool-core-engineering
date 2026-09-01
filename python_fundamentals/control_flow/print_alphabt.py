#!/usr/bin/env python3
buf = [chr(x) for x in range(ord('a'), ord('z')+1) if chr(x) not in "eq"]
print('{}'.format("".join(buf)), end="")
