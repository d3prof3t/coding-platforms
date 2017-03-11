"""
This module checks whether
the input string is a
palindrom or not
"""

my_str = input()

def check_palindrom(my_str):
    for k, v in enumerate(my_str):
        if (my_str[k] == my_str[-(1+(k*1))]):
            continue
        else:
            return "NO"
    return "YES"

print(check_palindrom(my_str))
