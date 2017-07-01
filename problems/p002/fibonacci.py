#!/usr/bin/python3

from itertools import count

def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 1) + fib(n - 2)
