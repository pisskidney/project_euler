#!/usr/bin/python
"""
What is the value of the first triangle number to have over five hundred
divisors?
"""

import math


def nr_divisors(k):
    x = 2
    prime_fact = dict()
    while k > 1:
        if k % x == 0:
            k /= x
            if x in prime_fact:
                prime_fact[x] += 1
            else:
                prime_fact[x] = 1
        else:
            x += 1
    nr_divisors = 1
    for k, v in prime_fact.iteritems():
        nr_divisors *= v + 1
    return nr_divisors


def main():
    x = 3
    i = 2
    while nr_divisors(x) < 500:
        i += 1
        x += i
    print x



if __name__ == "__main__":
    main()
