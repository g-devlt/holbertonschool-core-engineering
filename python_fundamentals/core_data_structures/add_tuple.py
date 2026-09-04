#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a[0:2][0] if len(tuple_a[0:2]) > 0 else 0
    a2 = tuple_a[0:2][1] if len(tuple_a[0:2]) > 1 else 0
    b1 = tuple_b[0:2][0] if len(tuple_b[0:2]) > 0 else 0
    b2 = tuple_b[0:2][1] if len(tuple_b[0:2]) > 1 else 0
    return (a1 + b1, a2 + b2)


if __name__ == "__main__":
    print(add_tuple((1, 2), (3, 4)))
    print(add_tuple((1, 2), (3,)))
    print(add_tuple((2, ), (3, 4)))
    print(add_tuple((), ()))
