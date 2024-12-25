
def next_secret_number(secret_number):
    mix_number = secret_number * 64
    secret_number = secret_number ^ mix_number
    secret_number = secret_number % 16777216

    mix_number = secret_number // 32
    secret_number = secret_number ^ mix_number
    secret_number = secret_number % 16777216

    mix_number = secret_number * 2048
    secret_number = secret_number ^ mix_number
    secret_number = secret_number % 16777216

    return secret_number

buyers = map(int, open("day22_input.txt").read().splitlines())

total = 0
for secret_number in buyers:

    for _ in range(2000):
        secret_number = next_secret_number(secret_number)

    total += secret_number

print(total)