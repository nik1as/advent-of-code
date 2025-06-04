lines = ""
while True:
    try:
        lines += input() + "\n"
    except EOFError:
        break
calories = lines.strip().split("\n\n")
calories = list(map(lambda x: list(map(int, x.split("\n"))), calories))

print(sum(max(calories, key=sum)))
