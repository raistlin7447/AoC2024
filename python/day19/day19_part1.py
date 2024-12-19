patterns_input, designs_input = open("day19_input.txt").read().split("\n\n")

patterns = patterns_input.split(", ")
designs = designs_input.split()

total = 0

for design in designs:
    length_matches = [True] + [False] * (len(design))

    for i in range(1, len(design) + 1):
        for pattern in patterns:
            if design[i - len(pattern):i] == pattern:
                length_matches[i] = length_matches[i] or length_matches[i - len(pattern)]

    if length_matches[len(design)]:
        total += 1

print(total)
