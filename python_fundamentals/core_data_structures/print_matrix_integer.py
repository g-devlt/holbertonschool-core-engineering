#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    [
        [
            print(
                ("{:d}").format(
                    coord
                ),
                end=" " if idx != (len(line) - 1) else "\n"
            )
            for idx, coord in enumerate(line)
        ] for line in matrix
    ]


if __name__ == "__main__":
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(m)
