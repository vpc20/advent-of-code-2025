from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    # rotations = read_input_to_text_array('aoc_01_testdata_01.txt')
    # rotations = read_input_to_text_array('aoc_01_testdata_02.txt') # test right rotation
    # rotations = read_input_to_text_array('aoc_01_testdata_03.txt') # test left rotation
    rotations = read_input_to_text_array('aoc_01_data_01.txt')

    position = 50
    pin = 0

    for e in rotations:
        direction = e[0]
        rotation_count = int(e[1:].strip())

        if direction == 'L':
            if position == 0:
                pin += (position + rotation_count) // 100
            elif position - rotation_count <= 0:
                pin += 1
                pin += (rotation_count - position) // 100
            position = (position - rotation_count) % 100
        else:
            pin += (position + rotation_count) // 100
            position = (position + rotation_count) % 100

    print(pin)
