import itertools

MOVES = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}

lines = ""
while True:
    try:
        lines += input() + "\n"
    except EOFError:
        break

grid, moves = lines.split("\n\n")
grid = list(map(list, grid.split("\n")))
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
    elif grid[new_y][new_x] == "O":
        border = False
        end = 0
        for i in itertools.count(start=2):
            x, y = robot_x + delta_x * i, robot_y + delta_y * i
            if grid[y][x] == "#":
                border = True
                break
            elif grid[y][x] == ".":
                end = i
                break

        if border:
            continue

        for k in range(end, 0, -1):
            x1, y1 = robot_x + delta_x * k, robot_y + delta_y * k
            x2, y2 = robot_x + delta_x * (k - 1), robot_y + delta_y * (k - 1)
            grid[y1][x1], grid[y2][x2] = grid[y2][x2], grid[y1][x1]
        robot_x, robot_y = new_x, new_y

result = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "O":
            result += 100 * y + x

for row in grid:
    print("".join(row))
print(result)
