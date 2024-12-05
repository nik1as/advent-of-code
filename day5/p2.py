def topological_sort(source):
    # https://stackoverflow.com/a/11564323
    pending = [(name, set(deps)) for name, deps in source]
    emitted = []
    while pending:
        next_pending = []
        next_emitted = []
        for entry in pending:
            name, deps = entry
            deps.difference_update(emitted)
            if deps:
                next_pending.append(entry)
            else:
                yield name
                emitted.append(name)
                next_emitted.append(name)
        if not next_emitted:
            raise ValueError
        pending = next_pending
        emitted = next_emitted


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
            graph = []
            for value in update:
                graph.append((value, {x for x, y in rules if y == value and x in update}))
            sort = list(topological_sort(graph))
            result += sort[len(sort) // 2]
            break

print(result)
