reports = []

while True:
    try:
        reports.append(list(map(int, input().split())))
    except EOFError:
        break

safe = 0
for report in reports:
    if any(sub_report == sorted(sub_report)
           and all(sub_report[i + 1] - sub_report[i] <= 3 and sub_report[i + 1] != sub_report[i] for i in range(len(sub_report) - 1))
           for sub_report in [report[:i] + report[i + 1:] for i in range(len(report))]):
        safe += 1
    if any(sub_report == sorted(sub_report, reverse=True)
           and all(sub_report[i] - sub_report[i + 1] <= 3 and sub_report[i + 1] != sub_report[i] for i in range(len(sub_report) - 1))
           for sub_report in [report[:i] + report[i + 1:] for i in range(len(report))]):
        safe += 1

print(safe)
