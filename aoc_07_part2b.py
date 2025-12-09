from aoc_tools import read_input_to_grid, print_grid_as_text


def count_timelines_dp_iterative(grid, start_pos):
    """
    True iterative bottom-up DP solution.
    Process rows from bottom to top, iterating each row until stable.

    Rules:
    - '.' cells: move down (r+1, c)
    - '^' cells: split left (r, c-1) and right (r, c+1)
    - Reaching the bottom row counts as 1 complete timeline
    """
    rows = len(grid)
    cols = len(grid[0])

    # Initialize DP table with 0s
    dp = [[0] * cols for _ in range(rows)]

    # Base case: bottom row '.' cells have 1 way
    for c in range(cols):
        if grid[rows - 1][c] == '.':
            dp[rows - 1][c] = 1

    # Process each row from bottom to top
    for r in range(rows - 2, -1, -1):
        # For rows with '^', we need to iterate until values stabilize
        # because '^' cells depend on same-row neighbors
        changed = True
        while changed:
            changed = False
            for c in range(cols):
                old_val = dp[r][c]
                new_val = 0

                if grid[r][c] == '.':
                    # '.' goes down
                    new_val = dp[r + 1][c]
                elif grid[r][c] == '^':
                    # '^' goes left and right
                    if c > 0:
                        new_val += dp[r][c - 1]
                    if c < cols - 1:
                        new_val += dp[r][c + 1]

                if new_val != old_val:
                    dp[r][c] = new_val
                    changed = True

    return dp[start_pos[0]][start_pos[1]]


def count_timelines_dp(grid, start_pos):
    """
    Top-down DP solution with memoization (cleaner for this problem).
    """
    rows = len(grid)
    cols = len(grid[0])

    dp = {}

    def compute(r, c):
        if (r, c) in dp:
            return dp[(r, c)]

        count = 0

        if grid[r][c] == '.':
            if r >= rows - 1:
                return 1
            count = compute(r + 1, c)
        elif grid[r][c] == '^':
            if c > 0:
                count += compute(r, c - 1)
            if c < cols - 1:
                count += compute(r, c + 1)

        dp[(r, c)] = count
        return count

    return compute(start_pos[0], start_pos[1])


def count_timelines_recursive(pos, grid, cache):
    """
    Original recursive solution with manual memoization.
    """
    if pos in cache:
        return cache[pos]

    r, c = pos
    count = 0

    if grid[r][c] == '.':
        if r >= len(grid) - 1:
            return 1
        count += count_timelines_recursive((r + 1, c), grid, cache)

    if grid[r][c] == '^':
        count += count_timelines_recursive((r, c - 1), grid, cache)
        count += count_timelines_recursive((r, c + 1), grid, cache)

    cache[pos] = count
    return count


if __name__ == '__main__':
    grid = read_input_to_grid('aoc_07_testdata_01.txt')
    # grid = read_input_to_grid('aoc_07_testdata_02.txt')
    # grid = read_input_to_grid('aoc_07_data_01.txt')
    print_grid_as_text(grid)

    # Find start position and replace 'S' with '.'
    start_pos = None
    for i, c in enumerate(grid[0]):
        if c == 'S':
            grid[0][i] = '.'  # change 'S' to space for processing
            start_pos = (0, i)
            break

    # Dynamic Programming solution (top-down with memoization)
    count_dp = count_timelines_dp(grid, start_pos)
    print(f"DP Solution (top-down): {count_dp}")

    # Iterative DP solution (true bottom-up)
    count_iter = count_timelines_dp_iterative(grid, start_pos)
    print(f"DP Solution (iterative): {count_iter}")

    # Recursive solution (for comparison)
    cache = {}
    count_rec = count_timelines_recursive(start_pos, grid, cache)
    print(f"Recursive Solution: {count_rec}")

    # Verify all give same answer
    assert count_dp == count_rec == count_iter, "Solutions don't match!"