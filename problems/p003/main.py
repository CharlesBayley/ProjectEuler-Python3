#!/usr/bin/python3
# Problem 3
# ---------
# Largest prime factor
# ====================
# The prime factors of 13195 are 5, 7, 13, and 29.
#
# What is the largest prime factor of the number `600851475143`?
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

def prime_gen():
    for i in count(0):
        if is_prime(i):
            yield i

def prime_factorize(n):
    factors = []
    for prime in prime_gen():
        if prime > n:
            break
        elif n % prime == 0:
            factors.append(prime)
            n /= prime
    return factors

def main():
    return max(prime_factorize(600851475143))

if __name__ == '__main__':
    print(main())
