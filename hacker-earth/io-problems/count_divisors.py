"""
This module counts the number of divisors
between two numbers of a third number
"""

my_nums = input()

nums = [int(c) for c in my_nums.split(' ')]

def divisors(start, stop, divisor):
    for i in range(start, stop):
        if i % divisor == 0:
            yield 1

print(sum(divisors(nums[0], nums[1]+1, nums[2])))
