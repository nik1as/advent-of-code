import re

DIGITS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

result = 0
for line in lines:
    matches = re.findall(rf"(?=(\d|{'|'.join(DIGITS.keys())}))", line)
    first = DIGITS.get(matches[0], matches[0])
    last = DIGITS.get(matches[-1], matches[-1])
    result += int(first + last)
print(result)
