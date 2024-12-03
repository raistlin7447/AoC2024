import re

f = open("day03_input.txt").read()

total = 0
for match in re.findall(r"mul\(?(\d+),?(\d+)\)", f):
    total += int(match[0]) * int(match[1])

print(total)