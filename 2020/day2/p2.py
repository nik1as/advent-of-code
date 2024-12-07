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

    if (password[min_amount - 1] == char) ^ (password[max_amount - 1] == char):
        valid += 1

print(valid)
