from collections import deque, defaultdict


def window(seq, n=2):
    it = iter(seq)
    win = deque((next(it, None) for _ in range(n)), maxlen=n)
    yield win
    append = win.append
    for e in it:
        append(e)
        yield win

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

buyer_diffs = []

for secret_number in buyers:
    current_price = secret_number % 10

    buyer_diff = [(current_price, None)]
    for _ in range(2000):
        secret_number = next_secret_number(secret_number)
        new_price = secret_number % 10
        buyer_diff.append((new_price, new_price - current_price))
        current_price = new_price

    buyer_diffs.append(buyer_diff)

four_sequences = defaultdict(int)

for buyer_diff in buyer_diffs:
    seen = set()
    for sliding_window in window(buyer_diff, 4):
        if sliding_window[0][1] is None:
            continue
        four_tuple = (sliding_window[0][1], sliding_window[1][1], sliding_window[2][1], sliding_window[3][1])
        if four_tuple in seen:
            continue
        seen.add(four_tuple)
        four_sequences[four_tuple] += sliding_window[3][0]

print(max(four_sequences.values()))