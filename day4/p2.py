lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

result = 0
for row in range(len(lines) - 2):
    for col in range(len(lines[row]) - 2):
        if ((lines[row][col] == "M" and lines[row + 1][col + 1] == "A" and lines[row + 2][col + 2] == "S")
            or (lines[row][col] == "S" and lines[row + 1][col + 1] == "A" and lines[row + 2][col + 2] == "M")) \
                and ((lines[row][col + 2] == "M" and lines[row + 1][col + 1] == "A" and lines[row + 2][col] == "S")
                     or (lines[row][col + 2] == "S" and lines[row + 1][col + 1] == "A" and lines[row + 2][col] == "M")):
            result += 1

print(result)
