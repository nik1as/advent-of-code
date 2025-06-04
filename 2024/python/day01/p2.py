left = []
right = []

while True:
    try:
        l, r = map(int, input().split())
        left.append(l)
        right.append(r)
    except EOFError:
        break

print(sum(e * right.count(e) for e in left))
