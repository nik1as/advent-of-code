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

tokens = 0
for machine in machines:
    machine = machine.strip()
    button_a, button_b, prize = machine.split("\n")
    a_x, a_y = map(int, BUTTON_A_PATTERN.search(button_a).groups())
    b_x, b_y = map(int, BUTTON_B_PATTERN.search(button_b).groups())
    dest_x, dest_y = map(int, PRIZE_PATTERN.search(prize).groups())
    dest_x, dest_y = dest_x + 10000000000000, dest_y + 10000000000000

    a = (dest_x * b_y - dest_y * b_x) / (a_x * b_y - a_y * b_x)
    b = (dest_x - a_x * a) / b_x

    if a % 1 == 0 and b % 1 == 0:
        tokens += 3 * int(a) + int(b)

print(tokens)
