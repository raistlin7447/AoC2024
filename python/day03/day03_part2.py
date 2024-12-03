import re

f = open("day03_input.txt").read()

cleaned = re.sub(r"don't\(\).*?(do\(\)|$)","", f, flags=re.DOTALL)

total = 0
for match in re.findall(r"mul\(?(\d+),?(\d+)\)", cleaned):
    total += int(match[0]) * int(match[1])

print(total)