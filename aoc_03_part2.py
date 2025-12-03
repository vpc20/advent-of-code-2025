from aoc_tools import read_input_to_text_array


def get_max_digit(s, maxlen):
    max_digit = 0
    digit_idx = 0
    for i, c in enumerate(s[:len(s) - maxlen + 1]):
        if int(c) > max_digit:
            max_digit = int(c)
            digit_idx = i
    return str(max_digit), digit_idx


if __name__ == '__main__':
    # joltages = read_input_to_text_array('aoc_03_testdata_01.txt')
    joltages = read_input_to_text_array('aoc_03_data_01.txt')

    total = 0
    for s in joltages:
        print('---------------------------------------------------------')
        print(s)
        idx = -1
        stemp = s
        digits_str = ''
        for maxlen in range(12, 0, -1):
            print(f"stemp '{stemp}'   maxlen  {maxlen}")
            max_digit, idx = get_max_digit(stemp, maxlen)
            stemp = stemp[idx + 1:]
            print(max_digit, idx)
            digits_str += max_digit
        print(digits_str)
        total += int(digits_str)

    print(total)
