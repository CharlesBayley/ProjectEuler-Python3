#!/usr/bin/python3
# Fibonacci sequence
#

def fib(n):
    p1 = 0
    p2 = 1
    next = p1
    for i in range(n):
        next = p1 + p2
        p1, p2 = p2, next
    return next
