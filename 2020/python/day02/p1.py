import re

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

pattern = re.compile(r"([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)")

valid = 0
for line in lines:
    match = re.match(pattern, line)
    min_amount = int(match.group(1))
    max_amount = int(match.group(2))
    char = match.group(3)
    password = match.group(4)

    if min_amount <= password.count(char) <= max_amount:
        valid += 1

print(valid)
