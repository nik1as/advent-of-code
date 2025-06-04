import math
import re

memory_dump = ""
while True:
    try:
        memory_dump += input()
    except EOFError:
        break

enabled = True
result = 0
for match in re.finditer(r"do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\)", memory_dump):
    instruction = match.group(0)
    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            result += math.prod(map(int, match.groups()))
print(result)
