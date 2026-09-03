#!/usr/bin/env python3

def pow(a, b):
    x = 1
    if (b > 0):
        for _ in range(b):
            x *= a
    elif (b < 0):
        x = float(x)
        for _ in range(-b):
            x = x / a
    return x


if __name__ == "__main__":
    print(pow(1, 9000))
    print(pow(2, 8)-1)
    print(pow(5, 4))
    print(pow(2, -2))
