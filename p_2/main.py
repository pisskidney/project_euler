#!/usr/bin/python
"""
By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""


def main():
    sum = 0
    x = 1
    y = 1
    while y < 4000000:
        if (not y & 1):
            sum += y
        x, y = y, x + y
    print sum


if __name__ == "__main__":
    main()
