disk_map = list(map(int, input()))

files = dict()  # file_id -> (file_position, file_size)
spaces = []  # (space_position, space_size)

file_id = 0
position = 0
for i in range(len(disk_map)):
    if i % 2 == 0:
        files[file_id] = (position, disk_map[i])
        file_id += 1
    elif disk_map[i] > 0:
        spaces.append((position, disk_map[i]))
    position += disk_map[i]

for file_id in range(len(files) - 1, -1, -1):
    file_position, file_size = files[file_id]

    found = None
    for i, (space_position, space_size) in enumerate(spaces):
        if space_position > file_position:
            break
        if space_size >= file_size:
            files[file_id] = (space_position, file_size)
            found = i, space_position, space_size
            break

    if found is not None:
        i, space_position, space_size = found
        if file_size == space_size:
            spaces.pop(i)
        else:
            spaces[i] = (space_position + file_size, space_size - file_size)

result = 0
for file_id, (file_position, file_size) in files.items():
    for i in range(file_position, file_position + file_size):
        result += file_id * i

print(result)
