left = []
right = []

while True:
    try:
        l, r = map(int, input().split())
        left.append(l)
        right.append(r)
    except EOFError:
        break

print(sum(abs(l - r) for l, r in zip(sorted(left), sorted(right))))
