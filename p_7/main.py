#!/usr/bin/python
import math
"""
Find the 10001st prime.
"""


def get_primes_upto(n):
    """
    Returns a list of all the prime numbers up to and including n
    Uses 'Stieve of Erastothenes' algorithm
    """
    hashmap = {}
    hashmap[0] = True
    hashmap[1] = True
    sqrt = int(math.ceil(math.sqrt(n)))
    for i in xrange(2, sqrt):
        if i not in hashmap:
            for j in xrange(i ** 2, n + 1, i):
                hashmap[j] = True
    return hashmap


def main():
    count = 0
    primes = get_primes_upto(1000000)
    for i in range(0, len(primes)):
        if not i in primes:
            count += 1
            if count == 10001:
                print i
                break


if __name__ == "__main__":
    main()
