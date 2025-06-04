depths = []
while True:
    try:
        depths.append(int(input()))
    except EOFError:
        break

print(sum(1 for prev, curr in zip(depths, depths[1:]) if curr > prev))
