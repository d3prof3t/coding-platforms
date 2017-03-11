"""
A simple module which inverts all the
cases of the characters present.
"""

my_str = input()

def toggle_case(my_str):
    for c in my_str:
        if c.islower():
            yield c.upper()
        elif c.isupper():
            yield c.lower()

for char in toggle_case(my_str):
    print(char, end='')
