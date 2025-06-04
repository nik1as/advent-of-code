import itertools
import re

LINE_PATTERN = re.compile(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)")
WIDTH = 101
HEIGHT = 103
SECONDS = 100

robots = []
while True:
    try:
        line = input()
        position_x, position_y, vel_x, vel_y = map(int, LINE_PATTERN.match(line).groups())
        robots.append((position_x, position_y, vel_x, vel_y))
    except EOFError:
        break

for s in itertools.count(start=1):
    for i in range(len(robots)):
        position_x, position_y, vel_x, vel_y = robots[i]
        new_x = (position_x + vel_x) % WIDTH
        new_y = (position_y + vel_y) % HEIGHT
        robots[i] = (new_x, new_y, vel_x, vel_y)

    result = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for robot in robots:
        result[robot[1]][robot[0]] += 1

    for y in range(HEIGHT):
        visited_positions = ["#" if result[y][i] > 0 else "." for i in range(WIDTH)]
        if "###############################" in "".join(visited_positions):
            print(s)
            for j in range(HEIGHT):
                print("".join("#" if result[j][i] > 0 else "." for i in range(WIDTH)))
            exit()
