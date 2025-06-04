import re

rules = []
while True:
    try:
        rules.append(input())
    except EOFError:
        break

graph = {}
for r in rules:
    color_primary = re.match(r"(.+?) bags", r).group(1)
    colors_inside = re.findall(r"(\d+) (.+?) bag", r)
    if len(colors_inside) > 0:
        graph[color_primary] = colors_inside
    else:
        graph[color_primary] = [("0", "")]


def count(color):
    if color == "":
        return 1
    return 1 + sum(int(amount) * count(child) for amount, child in graph[color])


print(count("shiny gold") - 1)
