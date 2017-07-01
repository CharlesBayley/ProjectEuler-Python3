#!/usr/bin/python3
# Prime Tools
# ===========
# These are all the simple functions/generators related to prime numbers
#

from itertools import count

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n / 2)):
        if n % i == 0:
            return False
    return True

def primes():
    for i in count(0):
        if is_prime(i):
            yield i

def factorize(n):
    factors = []
    for prime in primes():
        if prime > n:
            break
        elif n % prime == 0:
            factors.append(prime)
            n /= prime
    return factors
