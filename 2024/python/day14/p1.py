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

q1 = q2 = q3 = q4 = 0
for robot in robots:
    position_x, position_y, vel_x, vel_y = robot
    x, y = (position_x + vel_x * SECONDS) % WIDTH, (position_y + vel_y * SECONDS) % HEIGHT
    if x < WIDTH // 2 and y < HEIGHT // 2:
        q1 += 1
    elif x > WIDTH // 2 and y < HEIGHT // 2:
        q2 += 1
    elif x < WIDTH // 2 and y > HEIGHT // 2:
        q3 += 1
    elif x > WIDTH // 2 and y > HEIGHT // 2:
        q4 += 1

print(q1 * q2 * q3 * q4)
