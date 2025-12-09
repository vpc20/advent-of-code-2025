from functools import cache

from aoc_tools import read_input_to_grid, print_grid_as_text


@cache
def count_timelines(pos):
    r, c = pos
    count = 0

    if grid[r][c] == '.':
        if r >= len(grid) - 1:
            return 1
        count += count_timelines((r + 1, c))

    if grid[r][c] == '^':
        count += count_timelines((r, c - 1))
        count += count_timelines((r, c + 1))
    return count


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_07_testdata_01.txt')
    # grid = read_input_to_grid('aoc_07_testdata_02.txt')
    grid = read_input_to_grid('aoc_07_data_01.txt')

    print_grid_as_text(grid)

    i = 0
    for i, c in enumerate(grid[0]):
        if c == 'S':
            grid[0][i] = '.'  # change 'S' to space for processing below
            start_pos = (0, i)
            break
    # print(curr_pos)

    count = count_timelines(start_pos)
    print(count)
