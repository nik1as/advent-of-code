import itertools
import operator


def concat(a: int, b: int) -> int:
    return int(str(a) + str(b))


equations = []
while True:
    try:
        line = input()
        test_value, numbers = line.split(": ")
        test_value = int(test_value)
        numbers = list(map(int, numbers.split(" ")))
        equations.append((test_value, numbers))
    except EOFError:
        break

result = 0
for test_value, numbers in equations:
    for operators in itertools.product([operator.add, operator.mul, concat], repeat=len(numbers) - 1):
        value = numbers[0]
        for i in range(1, len(numbers)):
            value = operators[i - 1](value, numbers[i])
        if value == test_value:
            result += test_value
            break

print(result)
