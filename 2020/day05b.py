
# Advent of code day 5 part 2
# https://adventofcode.com/2020/day/5#part2

def check_boarding_pass(bp_code):

    upper = 0
    lower = 127
    count = 128

    for pos in range(0,7):

        selection = bp_code[pos]
        count = count / 2
        if selection == "F":
            lower -= count
        else:
            upper += count

    row = lower

    count = 8
    left = 0
    right = 7

    for pos in range(7,10):

        selection = bp_code[pos]
        count = count / 2
        if selection == "L":
            right -= count
        else:
            left += count

    column = left

    return (row, column)


with open("2020/day05_input.txt") as f:

    boarding_passes = {}
    seat_IDs = []

    for bp_code in f:

        bp_code = bp_code.strip()
        
        row, column = check_boarding_pass(bp_code)
        seat_id = int(row * 8 + column)
        # print("seat id is %d for boarding pass %s" % (seat_id, bp_code))

        boarding_passes[seat_id] = bp_code
        seat_IDs.append(seat_id)

seat_IDs.sort()

# show first 10 boarding passes
for seat_id in seat_IDs[:10]:
    print("%i %s" % (seat_id, boarding_passes[seat_id]))

print()

# show last 10 boarding passes
for seat_id in seat_IDs[-10:]:
    print("%i %s" % (seat_id, boarding_passes[seat_id]))

print("\n%i theoretical seats" % (128 * 8))
print("%i seats registered" % len(seat_IDs))
print("lowest seat id is %i" % min(seat_IDs))
print("highest seat id is %i" % max(seat_IDs))

# find gaps in seat IDs

for seat_id in range(0, 760):
    seat_a = seat_IDs[seat_id]
    seat_b = seat_IDs[seat_id+1]

    # there should only be a difference of 1 in the seat_IDs list
    difference = seat_b - seat_a

    # if there isn't, the missing seat has been found
    if difference != 1: 
        print("\ngap after seat id %i \nmissing seat id must be %i\n" % (seat_a, seat_a + 1))

        break

