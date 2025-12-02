# def count_pin(position, rotation_count):  # rotation direction is left
#     pin = 0
#     if position == 0:
#         pin = (position + rotation_count) // 100  # correct if position = 0
#     elif position - rotation_count <= 0:
#         pin = 1
#         pin += (rotation_count - position) // 100
#
#     return pin

def count_pin(position, rotation_count):  # rotation direction is left
    pin = 0

    q, r = divmod(rotation_count, 100)  # q is number of rotations
    pin += q
    if position == 0:
        if position - r >= 100:
            pin += 1
    else:
        if position - r <= 0:
            pin += 1

    return pin


position = 0
rotation_count = 1
assert count_pin(position, rotation_count) == 0

position = 0
rotation_count = 2
assert count_pin(position, rotation_count) == 0

position = 0
rotation_count = 99
assert count_pin(position, rotation_count) == 0

position = 0
rotation_count = 100
assert count_pin(position, rotation_count) == 1

position = 0
rotation_count = 101
assert count_pin(position, rotation_count) == 1

position = 0
rotation_count = 199
assert count_pin(position, rotation_count) == 1

position = 0
rotation_count = 200
assert count_pin(position, rotation_count) == 2

position = 0
rotation_count = 300
assert count_pin(position, rotation_count) == 3

position = 1
rotation_count = 1
assert count_pin(position, rotation_count) == 1

position = 1
rotation_count = 2
assert count_pin(position, rotation_count) == 1

position = 1
rotation_count = 99
assert count_pin(position, rotation_count) == 1

position = 1
rotation_count = 100
assert count_pin(position, rotation_count) == 1

position = 1
rotation_count = 101
assert count_pin(position, rotation_count) == 2

position = 1
rotation_count = 102
assert count_pin(position, rotation_count) == 2

position = 1
rotation_count = 199
assert count_pin(position, rotation_count) == 2

position = 1
rotation_count = 200
assert count_pin(position, rotation_count) == 2

position = 1
rotation_count = 201
assert count_pin(position, rotation_count) == 3

position = 1
rotation_count = 301
assert count_pin(position, rotation_count) == 4
