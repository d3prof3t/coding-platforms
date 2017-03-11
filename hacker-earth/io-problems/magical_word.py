"""
This module converts the strings
into magical strings using some
algorithm
"""

from math import sqrt

num_tests = int(input())

def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        k = round(sqrt(num))
        for i in range(2, k):
            if k % i == 0:
                return False
            continue
        return True


while num_tests > 0:
    str_len = int(input())
    my_str = input()
    if len(my_str) == str_len:
        for c in my_str:
            print(is_prime(ord(c)))
    num_tests -= 1

