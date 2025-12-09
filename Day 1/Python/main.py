import re


with open("puzzle_input.txt") as f:
    lines = [line.rstrip('\n') for line in f]


dial_position = 50 # 0-99
zero_count = 0
overlap_count = 0


def turn_left(rotation_amount):
    global dial_position, zero_count, overlap_count
    for _ in range(rotation_amount):
        dial_position -= 1
        if dial_position < 0:
            dial_position = 99
        if dial_position == 0:
            overlap_count += 1
    if dial_position == 0:
        zero_count += 1


def turn_right(rotation_amount):
    global dial_position, zero_count, overlap_count
    for _ in range(rotation_amount):
        dial_position += 1
        if dial_position > 99:
            dial_position = 0
        if dial_position == 0:
            overlap_count += 1
    if dial_position == 0:
        zero_count += 1


for l in lines:
    nl = re.split("(\d+)",l)
    if nl[0] == "L":
        turn_left(int(nl[1]))
    elif nl[0] == "R":
        turn_right(int(nl[1]))


print(f"The dial hit zero a total of {zero_count} times.")
print(f"Total times zero was seen through the rotations: {overlap_count}")