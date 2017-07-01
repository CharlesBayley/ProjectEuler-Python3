#!/usr/bin/python3
# Problem 4
# ---------
# Largest palindrome product
# ==========================
# A palindrome number reads the same way both ways. The largest palindrome
#  made from the product of two 2-digit numbers is `9009 = 91 * 99`
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

from .palindrome import is_palindrome

def main(lib):
    largest = 0
    for a in range(100, 1000):
        for b in range(a, 1000):
            ab = a * b
            if all([ab > largest, is_palindrome(ab)]):
                largest = ab
    return largest
