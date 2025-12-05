from copy import deepcopy

from aoc_tools import read_input_to_grid, print_grid_as_text


def count_adj_rolls(grid):
    adj_rolls_count = 0
    for dr, dc in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                   (r, c - 1), (r, c + 1),
                   (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
        if 0 <= dr < nrows and 0 <= dc < ncols and grid[dr][dc] == '@':
            adj_rolls_count += 1
    return adj_rolls_count


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_04_testdata_01.txt')
    grid = read_input_to_grid('aoc_04_data_01.txt')
    print_grid_as_text(grid)
    grid_copy = deepcopy(grid)

    nrows = len(grid)
    ncols = len(grid[0])
    xcount = 1
    total_xcount = 0

    while xcount > 0:
        xcount = 0
        index_list = []
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == '@':
                    adj_rolls_count = count_adj_rolls(grid)
                    if adj_rolls_count < 4:
                        xcount += 1
                        grid_copy[r][c] = '.'  # remove rolls from the copy of grid
        print(xcount)
        total_xcount += xcount

        # copy updated grid for next cycle processing
        grid = deepcopy(grid_copy)

    print(total_xcount)
    # 9243
