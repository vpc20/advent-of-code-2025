from collections import deque

from aoc_tools import read_input_to_grid, print_grid, print_grid_as_text

if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_07_testdata_01.txt')
    grid = read_input_to_grid('aoc_07_data_01.txt')

    print_grid_as_text(grid)

    q = deque()
    for i, c in enumerate(grid[0]):
        if c == 'S':
            q.append((0, i))
            break
    print(q)
    grid[0][i] = '.'  # change to space for processing below

    seen = set()
    split_set = set()
    while q:
        r, c = q.popleft()
        if (r, c) in seen:
            continue
        else:
            seen.add((r, c))


        while r < len(grid) and grid[r][c] == '.':
            r += 1

        if r < len(grid):
            assert grid[r][c] == '^'
            split_set.add((r,c))
            q.extend([(r, c - 1), (r, c + 1)])

    print(q)
    print(split_set)
    print(len(split_set))

    # 1703