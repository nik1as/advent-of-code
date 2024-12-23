depths = []
while True:
    try:
        depths.append(int(input()))
    except EOFError:
        break

windows = [sum(depths[i: i + 3]) for i in range(len(depths) - 2)]
print(sum(1 for prev, curr in zip(windows, windows[1:]) if curr > prev))
