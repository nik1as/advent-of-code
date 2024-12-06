import enum


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


grid = []
while True:
    try:
        grid.append(input())
    except EOFError:
        break

direction = Directions.UP
position = (0, 0)
for i, line in enumerate(grid):
    if "^" in line:
        position = (line.index("^"), i)
        break

visited = set()
visited.add(position)
while True:
    new_x, new_y = [sum(x) for x in zip(position, direction.value)]

    if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
        print(len(visited))
        break

    if grid[new_y][new_x] == "#":
        direction = Directions.turn_right(direction)
    else:
        position = (new_x, new_y)
        visited.add(position)
