import math
from collections import deque

SIZE = 71

byte_positions = []
while True:
    try:
        byte_positions.append(list(map(int, input().split(","))))
    except EOFError:
        break


def connected(blocked):
    distance = [[math.inf for _ in range(SIZE)] for _ in range(SIZE)]
    distance[0][0] = 0
    parents = dict()
    visited = [[False for _ in range(SIZE)] for _ in range(SIZE)]
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()
        if visited[y][x]:
            continue
        visited[y][x] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if new_x == SIZE - 1 and new_y == SIZE - 1:
                parents[(new_x, new_y)] = (x, y)
                return parents
            if 0 <= new_x < SIZE and 0 <= new_y < SIZE and not blocked[new_y][new_x]:
                queue.append((new_x, new_y))
                if distance[y][x] + 1 < distance[new_y][new_x]:
                    distance[new_y][new_x] = distance[y][x] + 1
                    parents[(new_x, new_y)] = (x, y)


def get_path(parents):
    path = set()
    curr_x, curr_y = SIZE - 1, SIZE - 1
    while True:
        parent = parents.get((curr_x, curr_y), None)
        if parent is None:
            break
        path.add(parent)
        curr_x, curr_y = parent
    return path


b = [[False for _ in range(SIZE)] for _ in range(SIZE)]
for x, y in byte_positions[:1024]:
    b[y][x] = True

p = get_path(connected(b))
for x, y in byte_positions[1024:]:
    b[y][x] = True
    if (x, y) not in p:
        continue
    result = connected(b)
    if result is None:
        print(f"{x},{y}")
        break
    p = get_path(result)
