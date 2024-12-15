from collections import deque

MOVES = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}
EXPANSION = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@."
}

lines = ""
while True:
    try:
        lines += input() + "\n"
    except EOFError:
        break

grid, moves = lines.split("\n\n")
grid = [list("".join(EXPANSION[char] for char in row)) for row in grid.split("\n")]
moves = moves.replace("\n", "")

robot_x, robot_y = 0, 0
for y in range(len(grid)):
    try:
        x = grid[y].index("@")
        robot_y = y
        robot_x = x
    except ValueError:
        continue

for move in moves:
    delta_x, delta_y = MOVES[move]
    new_x, new_y = robot_x + delta_x, robot_y + delta_y
    if grid[new_y][new_x] == "#":
        continue
    elif grid[new_y][new_x] == ".":
        grid[robot_y][robot_x], grid[new_y][new_x] = grid[new_y][new_x], grid[robot_y][robot_x]
        robot_x, robot_y = new_x, new_y
    elif grid[new_y][new_x] in ("[", "]"):
        queue = deque([(robot_x, robot_y)])
        seen = set()
        border = False
        while queue:
            x, y = queue.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            next_x, next_y = x + delta_x, y + delta_y
            if grid[next_y][next_x] == "#":
                border = True
                break
            elif grid[next_y][next_x] == "[":
                queue.append((next_x, next_y))
                queue.append((next_x + 1, next_y))
            elif grid[next_y][next_x] == "]":
                queue.append((next_x, next_y))
                queue.append((next_x - 1, next_y))

        if border:
            continue

        while seen:
            for x, y in list(seen):
                next_x, next_y = x + delta_x, y + delta_y
                if (next_x, next_y) not in seen:
                    grid[y][x], grid[next_y][next_x] = grid[next_y][next_x], grid[y][x]
                    seen.remove((x, y))
        robot_x, robot_y = new_x, new_y

result = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "[":
            result += 100 * y + x

for row in grid:
    print("".join(row))
print(result)
