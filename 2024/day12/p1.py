from collections import defaultdict

garden = []
while True:
    try:
        garden.append(list(input()))
    except EOFError:
        break

cords_by_type = defaultdict(set)
for y in range(len(garden)):
    for x in range(len(garden[y])):
        cords_by_type[garden[y][x]].add((y, x))


def get_region(y, x):
    type = garden[y][x]
    rows, cols = len(garden), len(garden[0])

    visited = set()
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        visited.add((y, x))
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < rows and 0 <= new_x < cols and garden[new_y][new_x] == type and (new_y, new_x) not in visited:
                stack.append((new_y, new_x))
    return visited


def get_price(region):
    rows, cols = len(garden), len(garden[0])

    area = len(region)
    perimeter = 0
    for y, x in region:
        type = garden[y][x]
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < rows and 0 <= new_x < cols and garden[new_y][new_x] != type:
                perimeter += 1
            if new_y < 0 or new_y >= rows or new_x < 0 or new_x >= cols:
                perimeter += 1

    return area * perimeter


price = 0
for type in cords_by_type.keys():
    cords = cords_by_type[type]
    while cords:
        visited = get_region(*cords.pop())
        cords.difference_update(visited)
        price += get_price(visited)
print(price)