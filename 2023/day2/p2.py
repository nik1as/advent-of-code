import math
import re
from collections import defaultdict

games = []
while True:
    try:
        line = input().split(": ")[1]
        records = re.split(",|;", line)
        for i, record in enumerate(records):
            count, color = record.strip().split(" ")
            records[i] = (int(count), color)
        games.append(records)
    except EOFError:
        break

result = 0
for i, game in enumerate(games, start=1):
    counts = defaultdict(int)
    for count, color in game:
        counts[color] = max(count, counts[color])
    result += math.prod(counts.values())
print(result)
