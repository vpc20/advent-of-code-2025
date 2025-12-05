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
                        index_list.append((r, c))
        print(xcount)
        print(index_list)
        total_xcount += xcount

        # update the grid
        for dr, dc in index_list:
            grid[dr][dc] = '.'
        # print_grid_as_text(grid)

    print(total_xcount)
    # 9243
