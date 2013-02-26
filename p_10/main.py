#!/usr/bin/python
"""
Find the sum of all the primes below two million.
"""

import math


def get_sieve(n):
    sieve = dict()
    sieve[0] = True
    sieve[1] = True
    for x in xrange(2, int(math.sqrt(n))):
        if x not in sieve:
            for y in xrange(x * 2, n, x):
                sieve[y] = True
    return sieve


def get_sum_primes_upto_2000000():
    sum = 0
    primes = get_sieve(2000000)
    for x in xrange(1, 2000000):
        if x not in primes:
            sum += x
    print sum


def main():
    get_sum_primes_upto_2000000()


if __name__ == "__main__":
    main()
