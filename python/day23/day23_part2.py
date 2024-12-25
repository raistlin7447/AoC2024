from collections import defaultdict, deque

connections = open("day23_input.txt").read().splitlines()
network = defaultdict(set)

for connection in connections:
    c1, c2 = connection.split("-")
    network[c1].add(c2)
    network[c2].add(c1)

groupings = set()
queue = deque([(computer, frozenset({computer})) for computer in network])

while queue:
    computer, current_group = queue.pop()
    for connected_computer in network[computer].difference(current_group):
        if network[connected_computer].issuperset(current_group):
            new_group = current_group.union({connected_computer})
            if new_group not in groupings:
                groupings.add(new_group)
                queue.append((connected_computer, new_group))

biggest_group = sorted(max(groupings, key=len))
print(",".join(biggest_group))
