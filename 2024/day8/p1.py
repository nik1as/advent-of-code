from collections import defaultdict

city_map = []
while True:
    try:
        city_map.append(input())
    except EOFError:
        break

antennas = defaultdict(list)
for y in range(len(city_map)):
    for x in range(len(city_map[y])):
        if city_map[y][x] != ".":
            antennas[city_map[y][x]].append((x, y))

antinodes = set()
for frequency, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            delta_x = x1 - x2
            delta_y = y1 - y2

            if 0 <= x1 + delta_x < len(city_map) and 0 <= y1 + delta_y < len(city_map[0]):
                antinodes.add((x1 + delta_x, y1 + delta_y))
            if 0 <= x2 - delta_x < len(city_map) and 0 <= y2 - delta_y < len(city_map[0]):
                antinodes.add((x2 - delta_x, y2 - delta_y))

print(len(antinodes))
