from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    # rotations = read_input_to_text_array('aoc_01_testdata_01.txt')
    rotations = read_input_to_text_array('aoc_01_data_01.txt')

    position = 50
    pin = 0

    for e in rotations:
        rotation_count = int(e.replace('L', '-')) if e[0] == 'L' else int(e.replace('R', '+'))
        position = (position + rotation_count) % 100
        if position == 0:
            pin += 1

    print(pin)
