import enum
from collections import defaultdict


class Directions(enum.Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)

    @staticmethod
    def turn_right(direction):
        if direction == Directions.UP:
            return Directions.RIGHT
        elif direction == Directions.RIGHT:
            return Directions.DOWN
        elif direction == Directions.DOWN:
            return Directions.LEFT
        else:
            return Directions.UP


def walk(grid, position):
    direction = Directions.UP

    visited = set()
    visited.add(position)
    directions = defaultdict(set)
    directions[position].add(direction)

    while True:
        new_x, new_y = [sum(e) for e in zip(position, direction.value)]
        new_position = (new_x, new_y)

        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            return visited, False

        if grid[new_y][new_x] == "#" or grid[new_y][new_x] == "O":
            direction = Directions.turn_right(direction)
            directions[position].add(direction)
        else:
            if new_position in visited and direction in directions[new_position]:
                return visited, True
            position = (new_x, new_y)
            visited.add(new_position)
            directions[new_position].add(direction)


grid = []
while True:
    try:
        grid.append(input())
    except EOFError:
        break

start_position = (0, 0)
for i, line in enumerate(grid):
    if "^" in line:
        start_position = (line.index("^"), i)
        break

visited, _ = walk(grid, start_position)

result = 0
for x, y in visited:
    if grid[y][x] == "^":
        continue

    new_grid = grid.copy()
    new_grid[y] = new_grid[y][:x] + "O" + new_grid[y][x + 1:]
    _, has_loop = walk(new_grid, start_position)
    if has_loop:
        result += 1

print(result)
