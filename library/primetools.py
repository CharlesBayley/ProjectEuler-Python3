#!/usr/bin/python3
# Prime Tools
# ===========
# These are all the simple functions/generators related to prime numbers
#

from itertools import count

def is_prime(n):
    if n < 2:
        return False
    elif n in [2, 3]:
        return True
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    yield 2
    yield 3
    def prime_guess():
        for i in count(1):
            yield 6*i - 1
            yield 6*i + 1
    for i in prime_guess():
        if is_prime(i):
            yield i

def factorize(n):
    factors = []
    for prime in primes():
        if prime > n:
            break
        while n % prime == 0:
            factors.append(prime)
            n /= prime
    return factors
