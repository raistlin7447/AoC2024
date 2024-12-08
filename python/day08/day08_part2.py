import itertools
from collections import defaultdict
from fractions import Fraction

map = [[i for i in line.strip()] for line in open("day08_input.txt").readlines()]

max_rows = len(map)
max_cols = len(map[0])

antennas = defaultdict(list)
antinodes = set()

for i, line in enumerate(map):
    for j, item in enumerate(line):
        if item != ".":
            antennas[item].append((i, j))
            antinodes.add((i, j))

for locations in antennas.values():
    pairs = itertools.permutations(locations, 2)
    for pair in pairs:
        distance = (pair[1][0] - pair[0][0], pair[1][1] - pair[0][1])
        antinode = (pair[0][0] - distance[0], pair[0][1] - distance[1])
        while 0 <= antinode[0] < max_rows and 0 <= antinode[1] < max_cols:
            antinodes.add(antinode)
            antinode = (antinode[0] - distance[0], antinode[1] - distance[1])

print(len(antinodes))
