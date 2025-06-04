import re

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

result = 0
for line in lines:
    matches = re.findall(r"\d", line)
    result += int(matches[0] + matches[-1])
print(result)
