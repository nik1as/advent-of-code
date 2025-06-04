disk_map = list(map(int, list(input())))

left = 0
right = len(disk_map) - 1

result = []
while left <= right:
    if left % 2 == 0:
        for _ in range(disk_map[left]):
            result.append(left // 2)
        left += 1
    else:
        if disk_map[left] == 0:
            left += 1
            continue
        result.append(right // 2)
        disk_map[right] -= 1
        disk_map[left] -= 1
        if disk_map[right] == 0:
            right -= 2
        if disk_map[left] == 0:
            left += 1

print(sum(i * result[i] for i in range(len(result))))
