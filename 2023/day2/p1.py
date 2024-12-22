import re

games = []
while True:
    try:
        line = input().split(": ")[1]
        records = re.split(",|;", line)
        for i, record in enumerate(records):
            count, color = record.strip().split(" ")
            records[i] = (int(count), color)
        games.append(records)
    except EOFError:
        break

result = 0
for i, game in enumerate(games, start=1):
    for count, color in game:
        if (color == "red" and count > 12) or (color == "green" and count > 13) or (color == "blue" and count > 14):
            break
    else:
        result += i
print(result)
