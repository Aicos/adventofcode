
# Advent of code day 5 
# https://adventofcode.com/2020/day/5

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

    seat_id = row * 8 + column

    print("seat id is %d" % seat_id)
    return seat_id


highest_seat_id = 0

with open("2020/day05_input.txt") as f:
    for line in f:
        seat_id = check_boarding_pass(line)
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
        
print("highest seat id is %d" % highest_seat_id)
