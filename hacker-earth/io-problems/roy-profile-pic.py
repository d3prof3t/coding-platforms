"""
This module is trying to tell
Roy if he can upload his pics
on Facebook or not based on
the given constraints.
"""

min_length = int(input())
num_pics = int(input())
pics_data = []

def decide_upload(x, y, min_length):
    if x < min_length or y < min_length:
        yield "UPLOAD ANOTHER"
    elif x >= min_length and y >= min_length:
        if x == y:
            yield "ACCEPTED"
        else:
            yield "CROP IT"

while num_pics > 0:
    dimensions = input()
    pics_data.append(tuple(dimensions.split(' ')))
    num_pics -= 1

for pic_data in pics_data:
    for decision in decide_upload(int(pic_data[0]), int(pic_data[1]), min_length):
        print(decision)
