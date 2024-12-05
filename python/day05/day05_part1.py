from collections import defaultdict

ordering, updates = open("day05_input.txt").read().split("\n\n")

forwards = defaultdict(set)
backwards = defaultdict(set)

for order in ordering.split("\n"):
    first, second = order.split("|")
    forwards[first].add(second)
    backwards[second].add(first)

total = 0
for update in updates.split("\n"):
    pages = update.split(",")

    fail = False
    for i in range(len(pages)):
        backwards_pages = pages[:i]
        forwards_pages = pages[i + 1:]

        for backwards_page in backwards_pages:
            if backwards_page not in backwards[pages[i]]:
                fail = True
                break

        if fail is True:
            break

        for forwards_page in forwards_pages:
            if forwards_page not in forwards[pages[i]]:
                fail = True
                break

    if fail is False:
        total += int(pages[len(pages) // 2])

print(total)