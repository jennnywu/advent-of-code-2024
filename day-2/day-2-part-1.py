with open("day-2/input.txt") as f:
    input = f.read().splitlines()

reports = [list(map(int, line.split())) for line in input]

def is_safe(levels):
    diffs = [b - a for a, b in zip(levels, levels[1:])]

    if any(d == 0 or abs(d) > 3 for d in diffs):
        return False
    
    return all(d > 0 for d in diffs) or all(d < 0 for d in diffs)

count = sum(is_safe(r) for r in reports)

print(f"day 2 part 1: {count}")