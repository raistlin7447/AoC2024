total = 0

def search_word(grid, word):
    rows, cols = len(grid), len(grid[0])

    def search_from(row, col, letter, d=None):
        global total
        if letter == len(word):
            return row, col

        if row < 0 or row >= rows or col < 0 or col >= cols:
            return None

        if grid[row][col] != word[letter]:
            return None

        if d:
            directions = [d]
        else:
            directions = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1) if not (i == j == 0)]
        for dr, dc in directions:
            result = search_from(row + dr, col + dc, letter + 1, (dr, dc))
            if result:
                total += 1

        return None

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == word[0]:
                search_from(row, col, 0)

    print(total)

grid = []
with open('day04_input.txt') as f:
    for line in f:
        grid.append(list(line.strip()))


word = 'XMAS'
search_word(grid, word)
