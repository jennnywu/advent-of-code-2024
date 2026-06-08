with open("day-4/input.txt") as f:
    input = f.read().splitlines()

word = 'XMAS'
total = 0

directions = [
    (0, 1),     # right
    (1, 0),     # down
    (0, -1),    # left
    (-1, 0),    # up
    (1, 1),     # down-right
    (1, -1),    # down-left
    (-1, 1),    # up-right
    (-1, -1)    # up-left
]

rows = len(input)
cols = len(input[0])

for r in range(rows):
    for c in range(cols):
        if input[r][c] != 'X':
            continue

        for dr, dc in directions:
            found = True

            for i in range(len(word)):
                nr = r + dr * i
                nc = c + dc * i

                if not (0 <= nr < rows and 0 <= nc < cols) or input[nr][nc] != word[i]:
                    found = False
                    break
            
            if found:
                total += 1

print(f"day 4 part 1: {total}")