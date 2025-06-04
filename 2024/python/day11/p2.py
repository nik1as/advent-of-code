import functools


@functools.cache
def blink(stone, blinks):
    if blinks == 0:
        return 1

    if stone == 0:
        return blink(1, blinks - 1)

    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        left = int(stone_str[:len(stone_str) // 2])
        right = int(stone_str[len(stone_str) // 2:])
        return blink(left, blinks - 1) + blink(right, blinks - 1)

    return blink(stone * 2024, blinks - 1)


numbers = list(map(int, input().split()))
print(sum(blink(stone, 75) for stone in numbers))
