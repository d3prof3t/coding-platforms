"""
This module calculates the product
of all numbers in the array
"""

def cal_product(arr):
    result = 1
    for num in arr:
        result *= int(num) % (10**9 +7)
    return result

my_array_len = int(input())
if my_array_len >= 1 and my_array_len <= 1000:
    my_array = input()
    my_array = my_array.split(' ')
    if len(my_array) == my_array_len:
        print(cal_product(my_array))


