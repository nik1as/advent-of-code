import math

seeds = map(int, input().split(": ")[1].split(" "))
categories = ""
while True:
    try:
        categories += input() + "\n"
    except EOFError:
        break
categories = categories.strip().split("\n\n")
category_to_mapping = dict()
for i in range(len(categories)):
    lines = categories[i].split("\n")
    from_category, to_category = lines[0].split(" map")[0].split("-to-")
    ranges = [tuple(map(int, line.split(" "))) for line in lines[1:]]
    category_to_mapping[from_category] = (to_category, ranges)

location = math.inf
for seed in seeds:
    current_category = "seed"
    while current_category != "location":
        to_category, ranges = category_to_mapping[current_category]
        for dest, src, length in ranges:
            if src <= seed < src + length:
                seed = (seed - src) + dest
                break
        current_category = to_category
    location = min(location, seed)
print(location)
