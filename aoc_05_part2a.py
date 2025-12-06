from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    # sections = read_input_to_sections('aoc_05_testdata_01.txt')
    sections = read_input_to_sections('aoc_05_data_01.txt')

    # for section in sections:
    #     print(section)
    #     print()

    id_ranges = []
    for line in sections[0].split():  # split text with '\n'
        start, end = line.split('-')
        id_ranges.append((int(start), int(end)))
    # print(id_ranges)

    id_ranges.sort()
    print(id_ranges)

    prev_start, prev_end = id_ranges[1]
    count_fresh_ids = prev_end - prev_start + 1
    print(prev_start, prev_end)
    print('count_fresh_ids', count_fresh_ids)

    for start, end in id_ranges[1:]:
        print(start, end)
        if end <= prev_end:  # whole range already counted
            continue
        if start <= prev_end:  # overlapping ranges
            start = prev_end + 1

        count_fresh_ids += end - start + 1
        prev_start = start
        prev_end = end
        print('count_fresh_ids', count_fresh_ids)

    print(count_fresh_ids)
    # 344423158480189 correct
