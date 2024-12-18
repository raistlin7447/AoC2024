from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(grid, start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    distance = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) == end:
                return distance

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy

                if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] == '.':
                    visited.add((new_x, new_y))
                    queue.append((new_x, new_y))

        distance += 1

    return -1


def solve_puzzle(byte_positions):
    size = 71
    grid = [['.' for _ in range(size)] for _ in range(size)]

    for byte_position in byte_positions:
        x, y = byte_position
        grid[x][y] = '#'

    start = (0, 0)
    end = (size - 1, size - 1)

    return bfs(grid, start, end)


byte_positions = [tuple(int(byte) for byte in line.strip().split(",")) for line in open("day18_input.txt").readlines()]

print(solve_puzzle(byte_positions[:1024]))
