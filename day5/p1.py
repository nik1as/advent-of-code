rules = []
updates = []
while True:
    line = input()
    if line == "":
        break
    rules.append(list(map(int, line.split("|"))))
while True:
    try:
        updates.append(list(map(int, input().split(","))))
    except EOFError:
        break

result = 0
for update in updates:
    for x, y in rules:
        if x in update and y in update and update.index(x) > update.index(y):
            break
    else:
        result += update[len(update) // 2]

print(result)
