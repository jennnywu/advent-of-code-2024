with open("day-4/input.txt") as f:
    input = f.read().splitlines()

total = 0

rows = len(input)
cols = len(input[0])

for r in range(1, rows - 1):
    for c in range(1, cols - 1):
        if input[r][c] != 'A':
            continue

        diagonal1 = input[r - 1][c - 1] + input[r][c] + input[r + 1][c + 1]
        diagonal2 = input[r - 1][c + 1] + input[r][c] + input[r + 1][c - 1]

        if diagonal1 in ("MAS", "SAM") and diagonal2 in ("MAS", "SAM"):
            total += 1

print(f"day 4 part 2: {total}")