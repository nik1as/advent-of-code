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
def check(design):
    if design == "":
        return True

    for pattern in patterns:
        if design.startswith(pattern) and check(design[len(pattern):]):
            return True
    return False


print(sum(1 for d in designs if check(d)))
