lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

x = 0
trees = 0
right = 3
for line in lines:
    if line[x] == "#":
        trees += 1
    x = (x + right) % len(lines[0])

print(trees)
