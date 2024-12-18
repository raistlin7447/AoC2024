from collections import deque
from copy import deepcopy

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(grid, start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)

    while queue:
        x, y = queue.popleft()

        if (x, y) == end:
            return True

        for dx, dy in directions:
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and (new_x, new_y) not in visited and grid[new_x][new_y] == '.':
                visited.add((new_x, new_y))
                queue.append((new_x, new_y))

    return False


def solve_puzzle(byte_positions):
    size = 71

    fresh_grid = [['.' for _ in range(size)] for _ in range(size)]
    start = (0, 0)
    end = (size - 1, size - 1)

    low = 0
    high = len(byte_positions) - 1
    result = None

    while low <= high:
        grid = deepcopy(fresh_grid)
        mid = (low + high) // 2

        for byte_position in byte_positions[:mid+1]:
            x, y = byte_position
            grid[x][y] = '#'

        if bfs(grid, start, end):
            low = mid + 1
        else:
            result = byte_positions[mid]
            high = mid - 1

    return result


byte_positions = [tuple(int(byte) for byte in line.strip().split(",")) for line in open("day18_input.txt").readlines()]

print(solve_puzzle(byte_positions))
