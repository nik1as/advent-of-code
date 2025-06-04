lines = []
while True:
    try:
        lines.append(input())
    except EOFError:
        break

trees = []
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
for right, down in slopes:
    t = 0
    x = 0
    y = 0
    while y < len(lines):
        if lines[y][x] == "#":
            t += 1
        y += down
        x = (x + right) % len(lines[0])
    trees.append(t)

product = 1
for t in trees:
    product *= t

print(product)
