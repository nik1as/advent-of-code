reports = []

while True:
    try:
        reports.append(list(map(int, input().split())))
    except EOFError:
        break

safe = 0
for report in reports:
    if report == sorted(report) and all(report[i + 1] - report[i] <= 3 and report[i + 1] != report[i] for i in range(len(report) - 1)):
        safe += 1
    if report == sorted(report, reverse=True) and all(report[i] - report[i + 1] <= 3 and report[i + 1] != report[i] for i in range(len(report) - 1)):
        safe += 1

print(safe)
