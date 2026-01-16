left = []
right = []

score = 0

with open("day-1/input.txt") as f:
    for line in f:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

freq = {}

for x in right:
    freq[x] = freq.get(x, 0) + 1

score = 0

for x in left:
    score += x * freq.get(x, 0)

print(f"day 1 part 2: {score}")