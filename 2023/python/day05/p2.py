segments = ""
while True:
    try:
        segments += input() + "\n"
    except EOFError:
        break
seeds, *categories = segments.strip().split("\n\n")
seeds = list(map(int, seeds.split("seeds: ")[1].split(" ")))
seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

category_to_mapping = dict()
for i in range(len(categories)):
    lines = categories[i].split("\n")
    from_category, to_category = lines[0].split(" map")[0].split("-to-")
    ranges = [tuple(map(int, line.split(" "))) for line in lines[1:]]
    category_to_mapping[from_category] = (to_category, ranges)

current_category = "seed"
while current_category != "location":
    to_category, ranges = category_to_mapping[current_category]
    new_seeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for dest, src, length in ranges:
            os = max(start, src)
            oe = min(end, src + length)
            if os < oe:
                new_seeds.append((os - src + dest, oe - src + dest))
                if os > start:
                    seeds.append((start, os))
                if end > oe:
                    seeds.append((oe, end))
                break
        else:
            new_seeds.append((start, end))
    seeds = new_seeds
    current_category = to_category

print(min(seeds)[0])
