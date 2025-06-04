import re
import string

grid = []
while True:
    try:
        grid.append(input())
    except EOFError:
        break

result = 0
for i, line in enumerate(grid):
    for match in re.finditer(r"\d+", line):
        start = match.start()
        end = match.end()

        adjacent = []
        if start > 0:
            adjacent.append((i, start - 1))
        if end < len(line) - 1:
            adjacent.append((i, end))
        if i > 0:
            for j in range(max(start - 1, 0), min(end + 1, len(line) - 1)):
                adjacent.append((i - 1, j))
        if i < len(grid) - 1:
            for j in range(max(start - 1, 0), min(end + 1, len(line) - 1)):
                adjacent.append((i + 1, j))

        if any(grid[y][x] not in "." + string.digits for y, x in adjacent):
            result += int(match.group())
print(result)
