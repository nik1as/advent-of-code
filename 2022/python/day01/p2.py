lines = ""
while True:
    try:
        lines += input() + "\n"
    except EOFError:
        break
calories = lines.strip().split("\n\n")
calories = list(map(lambda x: list(map(int, x.split("\n"))), calories))

top3 = sorted(calories, key=sum, reverse=True)[:3]
print(sum(map(sum, top3)))
