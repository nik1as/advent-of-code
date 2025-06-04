commands = []
while True:
    try:
        command, value = input().split()
        value = int(value)
        commands.append((command, value))
    except EOFError:
        break

horizontal = 0
depth = 0
aim = 0
for command, value in commands:
    if command == "forward":
        horizontal += value
        depth += aim * value
    elif command == "down":
        aim += value
    elif command == "up":
        aim -= value

print(horizontal * depth)
