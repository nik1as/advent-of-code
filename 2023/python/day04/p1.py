cards = []
while True:
    try:
        line = input()
        winning, numbers = line.split(": ")[1].split(" | ")
        winning = set(map(int, winning.split()))
        numbers = set(map(int, numbers.split()))
        cards.append((winning, numbers))
    except EOFError:
        break

points = 0
for i, (winning, numbers) in enumerate(cards, start=1):
    if match := winning & numbers:
        points += 2 ** (len(match) - 1)

print(points)
