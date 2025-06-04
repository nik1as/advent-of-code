import re

memory_dump = ""
while True:
    try:
        memory_dump += input()
    except EOFError:
        break

result = 0
for match in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", memory_dump):
    result += int(match.group(1)) * int(match.group(2))

print(result)
