seats = []
while True:
    try:
        seats.append(input())
    except EOFError:
        break

max_id = 0
for seat in seats:
    seat = seat.replace("\n", "")
    row = int(seat[:7].replace("F", "0").replace("B", "1"), 2)
    column = int(seat[7:].replace("L", "0").replace("R", "1"), 2)
    seat_id = row * 8 + column
    max_id = max(max_id, seat_id)

print(max_id)
