def is_safe(levels):
    if levels[0] > levels[1]:
        levels.reverse()

    for i in range(len(levels) - 1):
        if not(1 <= levels[i + 1] - levels[i] <= 3):
            return False
    return True

num_safe = 0
for report in open('day02_input.txt').readlines():
    levels = list(map(int, report.split()))

    if is_safe(levels):
        num_safe += 1
    else:
        for i in range(len(levels)):
            dampened_levels = levels.copy()
            del dampened_levels[i]
            if is_safe(dampened_levels):
                num_safe += 1
                break

print(num_safe)