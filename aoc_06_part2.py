import math

from aoc_tools import read_input_to_text_array_strip_n, print_grid


def compute_val(nums, ops):
    numsx = [[c for c in num] for num in zip(*nums)]
    print_grid(numsx)
    nums1 = [int(''.join(nums)) for nums in numsx]
    print(nums1)
    return sum(nums1) if ops == '+' else math.prod(nums1)


if __name__ == '__main__':
    # texts = read_input_to_text_array_strip_n('aoc_06_testdata_01.txt')
    texts = read_input_to_text_array_strip_n('aoc_06_data_01.txt')
    for e in texts:
        print(e)
    ops_str = texts[-1]
    print(ops_str)

    # indexes of the operators
    idxs = [i for i, c in enumerate(ops_str) if c != ' ']
    ops = [c for i, c in enumerate(ops_str) if c != ' ']
    print(idxs)

    nums2d = []
    for text in texts[:-1]:  # discard last line, it contains the operators
        start = 0
        end = 0
        nums = []
        for end in idxs[1:]:  # start with the second index
            substr = text[start:end - 1]
            nums.append(substr)
            start = end
        # nums.append(text[start:].ljust(len(text) - end + 1))
        nums.append(text[start:])
        # x = [      text[idxs[i - 1]:idxs[i] - 1] for i in range(1, len(idxs))        ]
        nums2d.append(nums)

    print('---------------------')
    total = 0
    for i, nums in enumerate(zip(*nums2d)):
        print(nums, ops[i])
        total += compute_val(nums, ops[i])
    print(total)

