import math
import re

BUTTON_A_PATTERN = re.compile(r"Button A: X\+(\d+), Y\+(\d+)")
BUTTON_B_PATTERN = re.compile(r"Button B: X\+(\d+), Y\+(\d+)")
PRIZE_PATTERN = re.compile(r"Prize: X=(\d+), Y=(\d+)")

machines = ""
while True:
    try:
        machines += input() + "\n"
    except EOFError:
        break

machines = machines.split("\n\n")

result = 0
for machine in machines:
    machine = machine.strip()
    button_a, button_b, prize = machine.split("\n")
    a_x, a_y = map(int, BUTTON_A_PATTERN.search(button_a).groups())
    b_x, b_y = map(int, BUTTON_B_PATTERN.search(button_b).groups())
    dest_x, dest_y = map(int, PRIZE_PATTERN.search(prize).groups())

    tokens = math.inf
    for a in range(101):
        for b in range(101):
            if a * a_x + b * b_x == dest_x and a * a_y + b * b_y == dest_y:
                tokens = min(tokens, 3 * a + b)

    if tokens != math.inf:
        result += tokens
print(result)
