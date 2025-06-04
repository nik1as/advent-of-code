numbers = []
while True:
    try:
        numbers.append(int(input()))
    except EOFError:
        break

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x + y + z == 2020:
                print(x * y * z)
                exit()
