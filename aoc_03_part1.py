from aoc_tools import read_input_to_text_array

if __name__ == '__main__':
    # joltages = read_input_to_text_array('aoc_03_testdata_01.txt')
    joltages = read_input_to_text_array('aoc_03_data_01.txt')

    total = 0
    for s in joltages:
        print(s)
        # first digit
        max_digit1 = 0
        maxi1 = 0
        for i, c in enumerate(s[:-1]):
            if int(c) > max_digit1:
                max_digit1 = int(c)
                max1i = i
        # second digit
        max_digit2 = 0
        for c in s[max1i + 1:]:
            max_digit2 = max(max_digit2, int(c))

        print(max_digit1, max_digit2)
        total += max_digit1 * 10 + max_digit2

    print(total)
