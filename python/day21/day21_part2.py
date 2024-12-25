from collections import defaultdict


def pad_lookup(pad_rows):
    coords = {}
    gap = '0,0' if len(pad_rows) == 2 else '3,0'

    for row, keys in enumerate(pad_rows):
        for col, key in enumerate(keys):
            if key != " ":
                coords[key] = [row, col]

    return {'coords': coords, 'gap': gap}

numeric_pad = pad_lookup(["789", "456", "123", " 0A"])
dir_pad = pad_lookup([" ^A", "<v>"])

def shortest_path(key1, key2, pad):
    r1, c1 = pad['coords'][key1]
    r2, c2 = pad['coords'][key2]

    ud = "v" * (r2 - r1) if r2 > r1 else "^" * (r1 - r2)
    lr = ">" * (c2 - c1) if c2 > c1 else "<" * (c1 - c2)

    if c2 > c1 and f"{r2},{c1}" != pad['gap']:
        # Safe to move vertically first if heading right and corner point isn't the gap
        return f"{ud}{lr}A"
    if f"{r1},{c2}" != pad['gap']:
        # Safe to move horizontally first if corner point isn't the gap
        return f"{lr}{ud}A"

    # Must be safe to move vertically first because we can't be in the same column as the gap.
    return f"{ud}{lr}A"

def sequences(seq, pad):
    keys = []
    prev_key = "A"
    for key in seq:
        keys.append(shortest_path(prev_key, key, pad))
        prev_key = key
    return keys

def complexity(codes, num_robots):
    # Frequency table of sub-sequences
    def seq_counts(seq):
        seq_list = sequences(seq, dir_pad)
        f_table = defaultdict(int)
        for s in seq_list:
            f_table[s] += 1
        return f_table

    # Start with the numeric keypad sequences
    f_tables = [defaultdict(int, {''.join(sequences(code, numeric_pad)): 1}) for code in codes]

    # Expand sequences for each robot
    for _ in range(num_robots):
        new_f_tables = []
        for f_table in f_tables:
            sub_f_table = defaultdict(int)
            for seq, freq in f_table.items():
                sub_seq_counts = seq_counts(seq)
                for sub_seq, sub_freq in sub_seq_counts.items():
                    sub_f_table[sub_seq] += sub_freq * freq
            new_f_tables.append(sub_f_table)
        f_tables = new_f_tables

    # Calculate the final complexity from each code's sequence frequencies
    def cmplx(seq):
        return sum(len(key) * freq for key, freq in seq.items())

    return sum(cmplx(seq) * int(code[:-1]) for seq, code in zip(f_tables, codes))

codes = open("day21_input.txt").read().splitlines()

print(complexity(codes, 25))
