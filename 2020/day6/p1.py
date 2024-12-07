groups = ""
while True:
    try:
        groups += input() + "\n"
    except EOFError:
        break

groups = groups.split("\n\n")

counts = []
for group in groups:
    counts.append(len(set(group.replace("\n", ""))))

print(sum(counts))
