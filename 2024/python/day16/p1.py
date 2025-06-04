import heapq

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
visited = {(start_x, start_y, 1, 0)}

while pqueue:
    cost, x, y, dx, dy = heapq.heappop(pqueue)
    visited.add((x, y, dx, dy))
    if grid[y][x] == "E":
        print(cost)
        break
    for new_cost, new_x, new_y, new_dx, new_dy in [(cost + 1, x + dx, y + dy, dx, dy), (cost + 1000, x, y, dy, -dx), (cost + 1000, x, y, -dy, dx)]:
        if grid[new_y][new_x] == "#":
            continue
        if (new_x, new_y, new_dx, new_dy) in visited:
            continue
        heapq.heappush(pqueue, (new_cost, new_x, new_y, new_dx, new_dy))
