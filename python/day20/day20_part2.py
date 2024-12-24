DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

grid = [list(row.strip()) for row in open("day20_input.txt").readlines()]

start = None
end = None
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            start = (r, c)
        elif grid[r][c] == 'E':
            end = (r, c)

baseline_path = [start]

while baseline_path[-1] != end:
    x, y = baseline_path[-1]
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in baseline_path and grid[nx][ny] != '#':
            baseline_path.append((nx, ny))
            break

total = 0
for i1, (x1, y1) in enumerate(baseline_path):
    for i2, (x2, y2) in enumerate(baseline_path):
        manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
        path_distance = i2 - i1
        time_save = path_distance - manhattan_distance
        if manhattan_distance <= 20 and time_save >= 100:
            total += 1

baseline = len(baseline_path)
print(total)
