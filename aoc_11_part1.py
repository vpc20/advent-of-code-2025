from collections import defaultdict
from functools import cache

# def count_paths(g, node, cache):
#     if node in cache:
#         return cache[node]
#     if node == 'out':
#         return 1
#
#     count = 0
#     for nb in g[node]:
#         count += count_paths(g, nb, cache)
#         cache[node] = count
#     return count


# @cache
# def count_paths(node):
#     count = 0
#     if node == 'out':
#         return 1
#     for nb in g[node]:
#         count += count_paths(nb)
#     return count


def count_paths(g, node):
    def count_paths_helper(node):
        nonlocal count
        if node == 'out':
            count += 1
            return
        for nb in g[node]:
            count_paths_helper(nb)


    count = 0
    count_paths_helper(node)
    return count

if __name__ == '__main__':
    # f = open('aoc_11_testdata_01.txt')
    f = open('aoc_11_data_01.txt')
    # create graph for the devices
    g = defaultdict(list)
    for line in f:
        dev_key, dev_vals = line.split(':')
        for val in dev_vals.split():
            g[dev_key].append(val)
    for k, v in g.items():
        print(k, v)
    f.close()

    count = count_paths(g, 'you')
    print(count)
