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

cards_count = [1 for _ in range(len(cards))]
for i, (winning, numbers) in enumerate(cards):
    matches = winning & numbers
    for j in range(i + 1, i + 1 + len(matches)):
        cards_count[j] += cards_count[i]

print(sum(cards_count))
