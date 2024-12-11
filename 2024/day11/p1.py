numbers = list(map(int, input().split()))

for _ in range(25):
    new_numbers = []
    for stone in numbers:
        if stone == 0:
            new_numbers.append(1)
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            left = int(stone_str[:len(stone_str) // 2])
            right = int(stone_str[len(stone_str) // 2:])
            new_numbers.append(left)
            new_numbers.append(right)
        else:
            new_numbers.append(stone * 2024)
    numbers = new_numbers

print(len(numbers))
