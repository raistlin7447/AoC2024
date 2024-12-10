from collections import deque

map = [[int(i) for i in row.strip()] for row in open("day10_input.txt")]

num_rows = len(map)
num_cols = len(map[0])

directions = [[1,0],[0,1],[-1,0],[0,-1]]
total = 0

for i, row in enumerate(map):
    for j, col in enumerate(row):
        if map[i][j] == 0:
            count = 0
            queue = deque([(i,j)])
            while queue:
                node = queue.popleft()
                height = map[node[0]][node[1]]

                if height == 9:
                    count += 1
                for direction in directions:
                    new = node[0] + direction[0], node[1] + direction[1]
                    if 0 <= new[0] < num_rows and 0 <= new[1] < num_cols:
                        if map[new[0]][new[1]] == height + 1:
                            queue.append(new)
            total += count

print(total)