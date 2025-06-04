import re

grid = []
while True:
    try:
        grid.append(input())
    except EOFError:
        break

nums = []
for y in range(len(grid)):
    nums.append([])
    for match in re.finditer(r"\d+", grid[y]):
        start = match.start() - 1
        end = match.end()
        num = int(match.group())
        nums[y].append((start, end, num))

result = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != "*":
            continue
        gears = []

        for k in (-1, 0, 1):
            if x + k < 0 or x + k >= len(grid[y]):
                continue

            for start, end, num in nums[y + k]:
                indices = list(range(start, end))
                if start <= x <= end:
                    gears.append(num)

        if len(gears) == 2:
            result += gears[0] * gears[1]
print(result)
