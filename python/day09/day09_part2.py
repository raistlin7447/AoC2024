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

first_free_space = 0
backward_ptr = len(disk) - 1

while backward_ptr > 0:
    while disk[backward_ptr] == ".":
        backward_ptr -= 1

    file_id = disk[backward_ptr]
    file_size = 0
    while disk[backward_ptr - file_size] == file_id:
        file_size += 1

    forward_ptr = first_free_space
    first_free = True
    while forward_ptr < backward_ptr:
        free_size = 0
        while disk[forward_ptr + free_size] == ".":
            if first_free:
                first_free = False
                first_free_space = forward_ptr
            free_size += 1

        if free_size >= file_size:
            for i in range(file_size):
                disk[forward_ptr + i] = disk[backward_ptr - i]
                disk[backward_ptr - i] = "."
            break
        else:
            forward_ptr += 1
    backward_ptr -= file_size

total = 0
for i, file_number in enumerate(disk):
    if file_number != ".":
        total += i * int(file_number)

print(total)
