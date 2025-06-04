numbers = []
while True:
    try:
        numbers.append(int(input()))
    except EOFError:
        break

for x in numbers:
    for y in numbers:
        if x + y == 2020:
            print(x * y)
            exit()
