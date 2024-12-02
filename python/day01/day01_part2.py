from collections import Counter

left = list()
right = list()

for line in open('day01_input.txt').readlines():
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

r_counter = Counter(right)

total = 0
for i in range(len(left)):
    total += left[i] * r_counter[left[i]]

print(total)
