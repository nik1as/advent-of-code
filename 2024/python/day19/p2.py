import functools

patterns = input().split(", ")
input()

designs = []
while True:
    try:
        designs.append(input())
    except EOFError:
        break


@functools.cache
def count(design):
    if design == "":
        return 1

    c = 0
    for pattern in patterns:
        if design.startswith(pattern):
            c += count(design[len(pattern):])
    return c


print(sum(map(count, designs)))
