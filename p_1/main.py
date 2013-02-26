#!/usr/bin/python
"""
Add all the natural numbers below one thousand that are multiples of 3 or 5.
"""


def main():
    print sum([i for i in xrange(3, 1000) if not i % 3 or not i % 5])


if __name__ == "__main__":
    main()
