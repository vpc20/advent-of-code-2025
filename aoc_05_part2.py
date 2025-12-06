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

    prev_start = id_ranges[0][0]
    prev_end = id_ranges[0][1]
    count_fresh_ids = prev_end - prev_start + 1
    print('count_fresh_ids', count_fresh_ids)

    for start, end in id_ranges[1:]:
        print(start, end)
        if end <= prev_end:
            continue  # whole range already counted
        if start > prev_end:
            count_fresh_ids += end - start + 1
            prev_start = start
        elif start < prev_end:
            count_fresh_ids += end - prev_end
            prev_start = prev_end
        else:
            count_fresh_ids += end - start
            prev_start = start + 1
        prev_end = end

        print('count_fresh_ids', count_fresh_ids)

    print(count_fresh_ids)
    # 332693433746707 too low
    # 332693433746726 too low
    # 344423158480189 correct

# (3, 5), (5, 10)
