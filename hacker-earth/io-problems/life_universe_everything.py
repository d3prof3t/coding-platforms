"""
This module will stop processing
input values after a particular
input value
"""

take_input = True
input_nums = []

while take_input:
    num = int(input())
    if num == 42:
        take_input = False
    else:
        input_nums.append(num)

for num in input_nums:
    print(num)
