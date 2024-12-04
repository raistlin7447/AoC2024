def search_grid(grid):
    rows, cols = len(grid), len(grid[0])
    total = 0

    def search_x(row, col):
        try:
            upper_left = grid[row - 1][col - 1]
            bottom_right = grid[row + 1][col + 1]

            upper_right = grid[row + 1][col - 1]
            bottom_left = grid[row - 1][col + 1]
        except IndexError:
            return False

        if sorted([upper_left, bottom_right]) == ["M", "S"] and sorted([upper_right, bottom_left]) == ["M", "S"]:
            return True
        else:
            return False

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "A":
                if search_x(row, col):
                    total += 1

    print(total)

grid = []
with open('day04_input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))

search_grid(grid)
