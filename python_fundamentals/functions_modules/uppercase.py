#!/usr/bin/env python3

def uppercase(str):
    if (not isinstance(str, type(""))):
        return
    print("{}".format(
        "".join(
            [
                chr(ord(x) - 0x20) if ord('a') <= ord(x) <= ord('z')
                else x for x in str
            ]
            )
        )
    )

if __name__ == "__main__":
    uppercase("name")
