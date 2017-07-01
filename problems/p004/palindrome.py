#!/usr/bin/python3
# Plaindrome Test
#

def is_palindrome(num):
    def reverse(con):
        return con[::-1]
    nums = str(num)
    return nums == reverse(nums)
