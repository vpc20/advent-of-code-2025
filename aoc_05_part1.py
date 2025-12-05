from aoc_tools import read_input_to_sections

if __name__ == '__main__':
    # sections = read_input_to_sections('aoc_05_testdata_01.txt')
    sections = read_input_to_sections('aoc_05_data_01.txt')

    # for section in sections:
    #     print(section)
    #     print()

    # id_ranges1 = [line.split('-') for line in sections[0].split()]
    # id_ranges2 = [(int(e[0]), int(e[1])) for e in id_ranges1]
    # id_ranges = [range(e[0], e[1] + 1) for e in id_ranges2]
    # print(id_ranges)

    id_ranges = []
    for line in sections[0].split():  # split text with '\n'
        start, end = line.split('-')
        id_ranges.append(range(int(start), int(end) + 1))
    # print(id_ranges)

    ids = [int(line.strip()) for line in sections[1].split()]
    # for id in ids:
    #     print(id)

    # fresh_count = 0
    # for id in ids:
    #     for id_range in id_ranges:
    #         if id in id_range:
    #             fresh_count += 1
    #             break
    # print(fresh_count)
    # 505

    # fresh_count = len([True for id in ids if any(id in id_range for id_range in id_ranges)])
    fresh_count = sum(1 for id in ids if any(id in id_range for id_range in id_ranges))
    print(fresh_count)
