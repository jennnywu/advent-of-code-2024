import re
import sys

with open("day-3/input.txt") as f:
    input = f.read().splitlines()

text = "".join(input)

token_re = re.compile(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)")

enabled = True
total = 0

for m in token_re.finditer(text):
    tok = m.group(0)

    if tok == "do()":
        enabled = True
    elif tok == "don't()":
        enabled = False
    else:
        if enabled:
            x = int(m.group(1))
            y = int(m.group(2))
            total += x * y

print(f"day 3 part 2: {total}")