import re

instructions = []
while True:
    try:
        instructions.append(input())
    except EOFError:
        break

pattern = re.compile("(acc|jmp|nop) ([+-][0-9]+)")

accomulator = 0
line = 0
executed_lines = set()
while line not in executed_lines:
    match = re.match(pattern, instructions[line])
    operation = match.group(1)
    argument = int(match.group(2))

    executed_lines.add(line)

    if operation == "acc":
        accomulator += argument
        line += 1
    elif operation == "jmp":
        line += + argument
    elif operation == "nop":
        line += 1

print(accomulator)
