import re

if __name__ == '__main__':
    # f = open('aoc_02_testdata_01.txt')
    f = open('aoc_02_data_01.txt')
    text = f.read()
    id_ranges = [[int(e.split('-')[0]), int(e.split('-')[1])] for e in text.split(',')]
    f.close()

    total = 0

    for start, end in id_ranges:
        print(start, end)
        for id in range(start, end + 1):
            sid = str(id)
            if len(sid) % 2 == 0:  # length should be an even number
                mid = len(sid) // 2
                if sid[0:mid] == sid[mid:]:
                    total += id
    print(total)
