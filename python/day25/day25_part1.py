from itertools import product
from operator import add

locks = []
keys = []

schematics = open("day25_input.txt").read().split("\n\n")

for schematic in schematics:
    bucket = None
    heights = [0] * 5
    for i, row in enumerate(schematic.splitlines()[:-1]):
        if i == 0:
            if row[0] == "#":
                bucket = locks
            else:
                bucket = keys
            continue

        for j, column in enumerate(row):
            if column == "#":
                heights[j] += 1

    bucket.append(heights)

total = 0
for lock, key in product(locks, keys):
    combined = map(add, lock, key)
    if max(combined) <= 5:
        total += 1

print(total)