import re

# check if the substrings of length slen repeats throughout the whole string
def is_repeating(s, slen):
    if len(s) % slen != 0:  # last string is shorter
        return False

    first_str = ''
    for i in range(0, len(s), slen):
        # print(i, i + slen)
        # print(s[i:i + slen])
        if i == 0:
            first_str = s[i:i + slen]
        else:
            if first_str != s[i:i + slen]:  # compare with subsequent strings
                return False
    return True


if __name__ == '__main__':
    # f = open('aoc_02_testdata_01.txt')
    f = open('aoc_02_data_01.txt')
    text = f.read()
    id_ranges = [[int(e.split('-')[0]), int(e.split('-')[1])] for e in text.split(',')]
    f.close()

    total = 0

    for start, end in id_ranges: # go through the range of ids
        print(start, end)
        for id in range(start, end + 1): # id is numeric
            sid = str(id)                # sid is the string representation of id
            mid = len(sid) // 2
            for slen in range(1, mid + 1):
                if is_repeating(sid, slen):
                    print('repeating', sid)
                    total += id
                    break
    print(total)
