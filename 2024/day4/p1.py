import re
from collections import defaultdict


def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return ["".join(row) for row in map(grouping.get, sorted(grouping))]


lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

result = 0
combinations = [groups(lines, lambda x, y: x),  # vertical
                groups(lines, lambda x, y: y),  # horizontal
                groups(lines, lambda x, y: x + y),  # diagonal (top-left -> bottom-right)
                groups(lines, lambda x, y: x - y)]  # diagonal (bottom-left -> top-right)
for comb in combinations:
    for line in comb:
        result += len(re.findall("XMAS", line))
        result += len(re.findall("XMAS", line[::-1]))

print(result)
