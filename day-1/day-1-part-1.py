left = []
right = []

total = 0

with open("day-1/input.txt") as f:
    for line in f:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))

left.sort()
right.sort()

for i in range(len(left)):
    total += abs(left[i] - right[i])

print(f"day 1 part 1: {total}")