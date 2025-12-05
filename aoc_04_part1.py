from aoc_tools import read_input_to_grid, print_grid_with_tabs, print_grid, print_grid_as_text


def count_adj_rolls(grid):
    adj_rolls_count = 0  # count adjacent rolls for each [row,col] position

    for dr, dc in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                   (r, c - 1), (r, c + 1),
                   (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
        if 0 <= dr < nrows and 0 <= dc < ncols and grid[dr][dc] == '@':
            adj_rolls_count += 1

    return adj_rolls_count


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_04_testdata_01.txt')
    grid = read_input_to_grid('aoc_04_data_01.txt')
    print_grid(grid)

    nrows = len(grid)
    ncols = len(grid[0])

    xcount = 0
    for r in range(nrows):
        for c in range(ncols):
            if grid[r][c] == '@':
                if count_adj_rolls(grid) < 4:
                    xcount += 1
    print(xcount)
    # 1460
