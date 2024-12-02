left = list()
right = list()

for line in open('day01_input.txt').readlines():
    l, r = line.split()
    left.append(int(l))
    right.append(int(r))

left.sort()
right.sort()

total = 0

for i in range(len(left)):
    total += abs(left[i] - right[i])

print(total)

