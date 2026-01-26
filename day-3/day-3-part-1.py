import re
import sys

with open("day-3/input.txt") as f:
    input = f.read().splitlines()

text = "".join(input)
pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
total = 0

for x, y in pattern.findall(text):
    total += int(x) * int(y)

print(f"day 3 part 1: {total}")