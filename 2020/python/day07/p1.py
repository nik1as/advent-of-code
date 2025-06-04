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


def contains_shiny(color):
    if color == "shiny gold":
        return True
    elif color == "":
        return False
    else:
        return any(contains_shiny(child) for amount, child in graph[color])


print(sum(contains_shiny(color) for color in graph.keys()) - 1)
