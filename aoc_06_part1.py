import math


def read_input_to_numsx(in_file):  # use this if all the inputs are numbers only
    f = open(in_file)

    arr2d = [[num for num in line.strip().split()] for line in f]
    nums = [[int(e) for e in row] for row in arr2d[:-1]]
    ops = arr2d[-1]

    f.close()
    return nums, ops


if __name__ == '__main__':
    # nums, ops = read_input_to_numsx('aoc_06_testdata_01.txt')
    nums, ops = read_input_to_numsx('aoc_06_data_01.txt')
    for e in nums:
        print(e)
    print(ops)

    zipped_nums = zip(*nums)  # transpose column to row

    total = 0
    for i, e in enumerate(zipped_nums):
        if ops[i] == '+':
            total += sum(e)
        else:
            total += math.prod(e)
    print(total)
    # 5733696195703

    # one-liner
    # print(sum(sum(e) if ops[i] == '+' else math.prod(e) for i, e in enumerate(zip(*nums))))
