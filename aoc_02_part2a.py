if __name__ == '__main__':
    # f = open('aoc_02_testdata_01.txt')
    f = open('aoc_02_data_01.txt')
    text = f.read()
    id_ranges = [[int(e.split('-')[0]), int(e.split('-')[1])] for e in text.split(',')]
    f.close()

    total = 0

    for start, end in id_ranges:  # go through the range of ids
        print(start, end)
        for id in range(start, end + 1):  # id is numeric
            sid = str(id)  # sid is the string representation of id
            mid = len(sid) // 2
            for slen in range(1, mid + 1):
                arr = [sid[i:i + slen] for i in range(0, len(sid), slen)]
                if all(arr[0] == arr[i] for i in range(1, len(arr))):
                    print('repeating', sid)
                    total += id
                    break
    print(total)
