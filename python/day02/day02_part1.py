num_safe = 0
for report in open('day02_input.txt').readlines():
    levels = list(map(int, report.split()))

    if levels[0] > levels[1]:
        levels.reverse()

    for i in range(len(levels) - 1):
        if not(1 <= levels[i + 1] - levels[i] <= 3):
            break
    else:
        num_safe += 1

print(num_safe)