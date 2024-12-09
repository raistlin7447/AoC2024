disk = []

file = True
file_number = 0
for l in open("day09_input.txt").read():
    if file:
        for i in range(int(l)):
            disk.append(str(file_number))
        file_number += 1
    else:
        disk += list("." * int(l))

    file = not file

forward_ptr = 0
backward_ptr = len(disk) - 1

while forward_ptr < backward_ptr:
    while disk[backward_ptr] == ".":
        backward_ptr -= 1

    if disk[forward_ptr] == ".":
        disk[forward_ptr] = disk[backward_ptr]
        disk[backward_ptr] = "."
    else:
        forward_ptr += 1

total = 0
for i, file_number in enumerate(disk[:backward_ptr+1]):
    total += i * int(file_number)

print(total)
