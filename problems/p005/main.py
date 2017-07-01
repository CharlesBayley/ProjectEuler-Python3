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

from multiset import Multiset

def main(lib):
    factorize = lib.primetools.factorize
    ms = Multiset([])
    for i in range(2, 21):
        ms |= Multiset(factorize(i))
    return reduce((lambda x,y: x*y), list(ms))
