with open("day-2/input.txt") as f:
    input = f.read().splitlines()

reports = [list(map(int, line.split())) for line in input]

def is_safe(levels):
    if len(levels) < 2:
        return True
    
    direction = 0

    for i in range(len(levels) - 1):
        diff = levels[i + 1] - levels[i]

        if diff == 0:
            return False
        
        if abs(diff) > 3:
            return False
        
        if direction == 0:
            direction = 1 if diff > 0 else -1
        else:
            if (diff > 0 and direction == -1) or (diff < 0 and direction == 1):
                return False
            
    return True

count = 0

for line in reports:
    if is_safe(line):
        count += 1
        continue

    for j in range(len(line)):
        if is_safe(line[:j] + line[j+1:]):
            count += 1
            break

print(f"day 2 part 2: {count}")