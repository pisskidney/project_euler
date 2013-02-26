#!/usr/bin/python
"""
What is the greatest product of four adjacent numbers in any direction (up,
down, left, right, or diagonally) in the 2020 grid?
"""


def read_matrix(filename):
    f = open(filename)
    data = list()
    for line in f:
        row = [int(nr) for nr in line.replace("\n", "").split(" ")]
        data.append(row)
    return data


def get_max_product(matrix, length=4):
    max_product = 0
    for i in xrange(0, len(matrix)):
        for j in xrange(0, len(matrix[0])):
            product_row = product_col = product_diag = product_diag2 = 1
            for x in xrange(0, length):
                try:
                    product_row *= matrix[i][j + x]
                except IndexError:
                    pass
                try:
                    product_col *= matrix[i + x][j]
                except IndexError:
                    pass
                try:
                    product_diag *= matrix[i + x][j + x]
                except IndexError:
                    pass
                try:
                    product_diag2 *= matrix[i + x][j - x]
                except IndexError:
                    pass
            product = max(
                product_row, product_col, product_diag, product_diag2
            )
            if product > max_product:
                max_product = product
    return max_product


def main():
    matrix = read_matrix("data.txt")
    print get_max_product(matrix, 4)


if __name__ == "__main__":
    main()
