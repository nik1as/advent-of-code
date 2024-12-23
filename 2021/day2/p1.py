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
for command, value in commands:
    if command == "forward":
        horizontal += value
    elif command == "down":
        depth += value
    elif command == "up":
        depth -= value

print(horizontal * depth)
