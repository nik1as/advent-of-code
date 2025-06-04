strategy = []
while True:
    try:
        strategy.append(tuple(input().split(" ")))
    except EOFError:
        break

scores = {
    ("A", "X"): 3,
    ("A", "Y"): 4,
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7,
}

print(sum(scores[round] for round in strategy))
