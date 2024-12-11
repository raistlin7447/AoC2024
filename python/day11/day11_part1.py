from functools import cache

@cache
def num_stones(value, iterations):
    if iterations == 0:
        return 1
    if value == "0":
        return num_stones("1", iterations - 1)
    if len(value) % 2 == 0:
        num_digits = len(value) // 2
        return num_stones(str(int(value[:num_digits])), iterations-1) + num_stones(str(int(value[num_digits:])), iterations-1)
    return num_stones(str(int(value) * 2024), iterations-1)

stones = open("day11_input.txt").read().split()
total = sum([num_stones(stone, 25) for stone in stones])
print(total)
