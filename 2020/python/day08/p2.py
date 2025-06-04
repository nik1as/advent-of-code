import re

instructions = []
while True:
    try:
        instructions.append(input())
    except EOFError:
        break

pattern = re.compile("(acc|jmp|nop) ([+-][0-9]+)")

for i in range(len(instructions)):
    accomulator = 0
    line = 0
    executed_lines = set()
    instructions_copy = instructions.copy()

    if instructions_copy[i].startswith("jmp"):
        instructions_copy[i] = instructions_copy[i].replace("jmp", "nop")
    elif instructions_copy[i].startswith("nop"):
        instructions_copy[i] = instructions_copy[i].replace("nop", "jmp")

    while line not in executed_lines:
        if line == len(instructions_copy) - 1:
            print(accomulator)
            quit()

        match = re.match(pattern, instructions_copy[line])
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
