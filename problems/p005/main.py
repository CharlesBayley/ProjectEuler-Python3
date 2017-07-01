#!/usr/bin/python3
# Problem 5
# ---------
# Smallest multiple
# =================
# 2520 is the smallest number that can be divided by each of the numbers from
#  1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by
#  all numbers from 1 to 20?
#

from functools import reduce

def main(lib):
    primes = lib.primetools.primes
    number = 1
    for prime in primes():
        print(prime)
        if prime > 10:
            break
        number *= prime
    return number
