seats = []
while True:
    try:
        seats.append(input())
    except EOFError:
        break

seat_ids = []
for seat in seats:
    seat = seat.replace("\n", "")
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat[7:].replace("L", "0").replace("R", "1"), 2)

    seat_id = row * 8 + column
    seat_ids.append(seat_id)

seat_ids.sort()
print((set(range(seat_ids[0], seat_ids[-1])) - set(seat_ids)).pop())
