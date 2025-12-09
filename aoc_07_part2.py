from collections import deque, defaultdict

from aoc_tools import read_input_to_grid, print_grid_as_text


def dfs(graph, start_pos):
    def dfs_aux(pos):
        nonlocal timeline_count
        # print(pos)
        # if pos[0] == 15:
        if pos[0] == 141:
            timeline_count += 1
            print(timeline_count)
        for next_pos in graph[pos]:
            dfs_aux(next_pos)
        return

    timeline_count = 0
    dfs_aux(start_pos)
    return timeline_count


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_07_testdata_01.txt')
    grid = read_input_to_grid('aoc_07_data_01.txt')

    print_grid_as_text(grid)

    i = 0
    for i, c in enumerate(grid[0]):
        if c == 'S':
            grid[0][i] = '.'  # change 'S' to space for processing below
            start_pos = (0, i)
            break
    # print(curr_pos)

    # create the graph (tree)
    graph = defaultdict(set)
    q = deque()
    curr_pos = start_pos
    q.append(curr_pos)
    seen = set()
    while q:
        r, c = q.popleft()
        curr_pos = (r, c)
        if (r, c) in seen:
            continue
        else:
            seen.add((r, c))

        while r < len(grid) and grid[r][c] == '.':
            r += 1
            if r < len(grid):
                graph[curr_pos].add((r, c))
                curr_pos = (r, c)

        if r < len(grid):
            assert grid[r][c] == '^'
            q.extend([(r, c - 1), (r, c + 1)])
            graph[curr_pos].add((r, c - 1))
            graph[curr_pos].add((r, c + 1))

    for k, v in graph.items():
        print(k, v)
    count = dfs(graph, start_pos)
    print(count)
