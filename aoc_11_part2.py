from collections import defaultdict, deque
from functools import cache


def is_directed_acyclic_dfs(g, u):
    def dfs(g, u):
        seen.add(u)
        cycles.add(u)
        for v in g[u]:
            if v not in seen:
                if not dfs(g, v):
                    return False
            elif v in cycles:  # back edge
                return False
        cycles.remove(u)
        return True

    seen = set()
    cycles = set()
    for u in list(g.keys()):
        print(u)
        if u not in seen:
            if not dfs(g, u):
                return False
    return True


def count_paths_dp(g, start, end):
    """Count paths using dynamic programming (memoization)"""
    memo = {}

    def dp(node):
        # Base case
        if node == end:
            return 1

        # Check memo
        if node in memo:
            return memo[node]

        # Count paths through neighbors
        total = 0
        for neighbor in g[node]:
            total += dp(neighbor)

        memo[node] = total
        return total

    return dp(start)


# def count_paths(g, curr, end, cache={}): # incorrect the value of cache is carried over to the next function call
#     count = 0                            # dictionaries are mutable
#     if curr == end:
#         return 1
#     if curr in cache:
#         return cache[curr]
#
#     for nb in g[curr]:
#         count += count_paths(g, nb, end, cache)
#     cache[curr] = count
#     return count

# def count_paths(g, curr, end, cache=None):
#     if cache is None:
#         cache = {}
#     if curr == end:
#         return 1
#     if curr in cache:
#         return cache[curr]
#
#     count = 0
#     for nb in g[curr]:
#         count += count_paths(g, nb, end, cache)
#     cache[curr] = count
#     return count


# @cache
# def count_paths(node, end):
#     count = 0
#     if node == end:
#         return 1
#     for nb in g[node]:
#         count += count_paths(nb, end)
#     return count

def count_paths(g, node, end):
    @cache
    def dfs(node, end):
        if node == end:
            return 1

        count = 0
        for nb in g[node]:
            count += dfs(nb, end)
        return count

    return dfs(node, end)


# def count_paths(g, node, end):  # incorrect
#     def count_paths_helper(node, seen):
#         nonlocal count
#         if node == end:
#             count += 1
#             return
#         for nb in g[node]:
#             if node not in seen:
#                 seen.add(node)
#                 count_paths_helper(nb, seen)
#                 seen.remove(node)
#
#     seen = {node}
#     count = 0
#     count_paths_helper(node, seen)
#     return count

def get_all_paths(g, start, end):
    def get_helper(curr, end, path):
        nonlocal paths
        if curr == end:
            paths.append(path)

        for nb in g[curr]:
            if nb not in path:  # Avoid cycles
                get_helper(nb, end, path + [nb])

    paths = []
    get_helper(start, end, [start])
    return paths


# def get_all_paths(g, start, end, path=None):
#     """Get all actual paths (for verification/visualization)"""
#     if path is None:
#         path = []
#
#     path = path + [start]
#
#     if start == end:
#         return [path]
#
#     paths = []
#     for nb in g[start]:
#         if nb not in path:  # Avoid cycles
#             new_paths = get_all_paths(g, nb, end, path)
#             paths.extend(new_paths)
#
#     return paths

def bfs_all_paths1(g, source, target):
    paths = []
    q = deque([(source, [source])])
    while q:
        v, path = q.popleft()
        for nb in g[v]:
            if nb == target:
                paths.append(path + [nb])
                continue
            if nb not in path:
                q.append((nb, path + [nb]))
    return paths


if __name__ == '__main__':
    # f = open('aoc_11_testdata_01.txt')
    # f = open('aoc_11_testdata_02.txt')
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

    # count = count_paths(g, 'fft')
    # print(count)
    # 8281 too low

    print(is_directed_acyclic_dfs(g, 'svr'))
    print(count_paths_dp(g, 'svr', 'out'))
    print(count_paths(g, 'svr', 'out'))

    print(count_paths_dp(g, 'svr', 'dac') * count_paths_dp(g, 'dac', 'fft') * count_paths_dp(g, 'fft', 'out'))
    print(count_paths_dp(g, 'svr', 'fft') * count_paths_dp(g, 'fft', 'dac') * count_paths_dp(g, 'dac', 'out'))

    print(count_paths(g, 'svr', 'dac') * count_paths(g, 'dac', 'fft') * count_paths(g, 'fft', 'out'))
    print(count_paths(g, 'svr', 'fft') * count_paths(g, 'fft', 'dac') * count_paths(g, 'dac', 'out'))

    # paths = get_all_paths(g, 'svr', 'out')
    # for path in paths:
    #     print(path)
    #
    # print()
    # for item in bfs_all_paths1(g, 'svr', 'out'):
    #     print(item)

