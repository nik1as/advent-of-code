import math
from collections import deque

SIZE = 71

blocked = [[False for _ in range(SIZE)] for _ in range(SIZE)]
count = 0
while True:
    try:
        if count >= 1024:
            break
        x, y = map(int, input().split(","))
        blocked[y][x] = True
        count += 1
    except EOFError:
        break

distance = [[math.inf for _ in range(SIZE)] for _ in range(SIZE)]
distance[0][0] = 0
visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()
    if visited[y][x]:
        continue
    visited[y][x] = True
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < SIZE and 0 <= new_y < SIZE and not blocked[new_y][new_x]:
            queue.append((new_x, new_y))
            distance[new_y][new_x] = min(distance[new_y][new_x], distance[y][x] + 1)

print(distance[SIZE - 1][SIZE - 1])
