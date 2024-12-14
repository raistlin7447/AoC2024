import re

machines = open("day13_input.txt").read().split("\n\n")

total = 0
for machine in machines:
    rows = machine.split("\n")
    a_x, a_y = map(int, re.match(r"Button A: X\+(\d+), Y\+(\d+)", rows[0]).groups())
    b_x, b_y = map(int, re.match(r"Button B: X\+(\d+), Y\+(\d+)", rows[1]).groups())
    p_x, p_y = map(int, re.match(r"Prize: X=(\d+), Y=(\d+)", rows[2]).groups())

    b_presses = (p_y * a_x - p_x * a_y) / (b_y * a_x - b_x * a_y)
    a_presses = (p_x - b_presses * b_x) / a_x

    if a_presses.is_integer() and b_presses.is_integer():
        total += a_presses * 3 + b_presses

print(int(total))