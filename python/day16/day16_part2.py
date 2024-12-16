from queue import PriorityQueue

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def solve_maze(maze):
    rows, cols = len(maze), len(maze[0])

    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    pq = PriorityQueue()
    dist = [[[float('inf')] * 4 for _ in range(cols)] for _ in range(rows)]

    pq.put((0, start[0], start[1], 0, [(start[0], start[1])]))
    dist[start[0]][start[1]][0] = 0
    best_path_tiles = set()
    best_cost = float('inf')

    while not pq.empty():
        cost, x, y, direction, path = pq.get()

        if cost > best_cost:
            continue

        if (x, y) == end:
            best_cost = cost
            best_path_tiles = best_path_tiles.union(path)
            continue

        for i in range(4):
            new_dir = (direction + i) % 4
            new_x = x + directions[new_dir][0]
            new_y = y + directions[new_dir][1]

            if 0 <= new_x < rows and 0 <= new_y < cols and maze[new_x][new_y] != '#':
                new_cost = dist[x][y][direction]
                if direction == new_dir:
                    new_cost += 1
                else:
                    new_cost += 1001

                if dist[new_x][new_y][new_dir] >= new_cost:
                    dist[new_x][new_y][new_dir] = new_cost
                    pq.put((new_cost, new_x, new_y, new_dir, path + [(new_x, new_y)]))

    return len(best_path_tiles)


maze = [i.strip() for i in open('day16_input.txt').readlines()]

cost = solve_maze(maze)
print(cost)
