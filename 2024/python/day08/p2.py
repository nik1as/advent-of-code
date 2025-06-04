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
            antinodes.add(positions[i])
            antinodes.add(positions[j])

            x1, y1 = positions[i]
            x2, y2 = positions[j]

            delta_x = x1 - x2
            delta_y = y1 - y2

            k = 1
            while True:
                antinode_x = x1 + delta_x * k
                antinode_y = y1 + delta_y * k
                if not (0 <= antinode_x < len(city_map) and 0 <= antinode_y < len(city_map[0])):
                    break
                antinodes.add((antinode_x, antinode_y))
                k += 1

            k = -1
            while True:
                antinode_x = x1 + delta_x * k
                antinode_y = y1 + delta_y * k
                if not (0 <= antinode_x < len(city_map) and 0 <= antinode_y < len(city_map[0])):
                    break
                antinodes.add((antinode_x, antinode_y))
                k -= 1

print(len(antinodes))
