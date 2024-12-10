topographic_map = []
while True:
    try:
        topographic_map.append(list(map(int, input())))
    except EOFError:
        break


def hike(row, col, height=0):
    if height == 9:
        return 1

    result = 0
    if row > 0 and topographic_map[row - 1][col] == height + 1:
        result += hike(row - 1, col, height + 1)
    if row < len(topographic_map) - 1 and topographic_map[row + 1][col] == height + 1:
        result += hike(row + 1, col, height + 1)
    if col > 0 and topographic_map[row][col - 1] == height + 1:
        result += hike(row, col - 1, height + 1)
    if col < len(topographic_map[0]) - 1 and topographic_map[row][col + 1] == height + 1:
        result += hike(row, col + 1, height + 1)
    return result


trailheads = []
for row in range(len(topographic_map)):
    for col in range(len(topographic_map[0])):
        if topographic_map[row][col] == 0:
            trailheads.append((row, col))

print(sum(hike(row, col) for row, col in trailheads))
