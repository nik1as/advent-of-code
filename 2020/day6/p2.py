groups = ""
while True:
    try:
        groups += input() + "\n"
    except EOFError:
        break

groups = [e.strip() for e in groups.split("\n\n")]

counts = []
for group in groups:
    common_answers = set(group.split("\n")[0])
    for answers in group.split("\n"):
        common_answers.intersection_update(set(answers))
    counts.append(len(common_answers))

print(sum(counts))
