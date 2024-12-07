import itertools
from operator import add, mul

def concat(a, b):
    return int(f"{a}{b}")

equations = open("day07_input.txt").readlines()

total = 0

for equation in equations:
    answer, n = equation.strip().split(":")
    numbers = list(map(int, n.strip().split(" ")))
    attempts = len(numbers) - 1
    options = itertools.product([add, mul, concat], repeat=attempts)

    for o in options:
        test_answer = o[0](numbers[0], numbers[1])
        for i, number in enumerate(numbers[2:], start=1):
            test_answer = o[i](test_answer, number)
        if test_answer == int(answer):
            total += test_answer
            break

print(total)