#!/usr/bin/python3
# Problem 1
# ---------
# Multiples of 3 and 5
# ====================
# If we list of the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6, and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.
#

def main():
    sum = 0
    for i in range(1000):
        if any([i % 3 == 0, i % 5 == 0]):
            sum += i
    return sum

if __name__ == '__main__':
    print(main())
