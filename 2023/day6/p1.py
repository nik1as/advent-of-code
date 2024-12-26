import math
import re

time = []
for match in re.finditer(r"\d+", input()):
    time.append(int(match.group()))

distance = []
for match in re.finditer(r"\d+", input()):
    distance.append(int(match.group()))

counts = []
for t, d in zip(time, distance):
    c = 0
    for i in range(0, t + 1):
        distance = (t - i) * i
        if distance > d:
            c += 1
    counts.append(c)

print(math.prod(counts))
