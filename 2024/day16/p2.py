import heapq
import math
from collections import defaultdict, deque

grid = []
while True:
    try:
        grid.append(list(input()))
    except EOFError:
        break

rows = len(grid)
cols = len(grid[0])

for y in range(rows):
    for x in range(cols):
        if grid[y][x] == "S":
            start_x, start_y = x, y
            break
    else:
        continue
    break

pqueue = [(0, start_x, start_y, 1, 0)]  # (cost, x, y, dx, dy)
lowest_cost = defaultdict(lambda: math.inf)
lowest_cost[(start_x, start_y, 1, 0)] = 0
best_score = math.inf
parents = defaultdict(set)
end_states = set()

while pqueue:
    cost, x, y, dx, dy = heapq.heappop(pqueue)
    if cost > lowest_cost[(x, y, dx, dy)]:
        continue
    if grid[y][x] == "E":
        if cost > best_score:
            break
        best_score = cost
        end_states.add((x, y, dx, dy))
    for new_cost, new_x, new_y, new_dx, new_dy in [(cost + 1, x + dx, y + dy, dx, dy), (cost + 1000, x, y, dy, -dx), (cost + 1000, x, y, -dy, dx)]:
        if grid[new_y][new_x] == "#":
            continue
        lowest = lowest_cost[(new_x, new_y, new_dx, new_dy)]
        if new_cost > lowest:
            continue
        if new_cost < lowest:
            parents[(new_x, new_y, new_dx, new_dy)] = set()
            lowest_cost[(new_x, new_y, new_dx, new_dy)] = new_cost
        parents[(new_x, new_y, new_dx, new_dy)].add((x, y, dx, dy))
        heapq.heappush(pqueue, (new_cost, new_x, new_y, new_dx, new_dy))

states = deque(end_states)
visited = set(end_states)
while states:
    state = states.popleft()
    for parent in parents[state]:
        if parent in visited:
            continue
        visited.add(parent)
        states.append(parent)

print(len({(x, y) for x, y, _, _ in visited}))
