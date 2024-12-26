import re

time = int("".join(match.group() for match in re.finditer(r"\d+", input())))
distance = int("".join(match.group() for match in re.finditer(r"\d+", input())))

l, r = 0, time
while l < r:
    mid = (l + r) // 2
    if (time - mid) * mid > distance:
        r = mid
    else:
        l = mid + 1

from_time = l

l, r = 0, time
while l < r:
    mid = (l + r) // 2
    if (time - mid) * mid < distance:
        r = mid
    else:
        l = mid + 1

print(l - from_time)
