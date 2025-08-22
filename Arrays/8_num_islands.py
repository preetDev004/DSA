from typing import List
from collections import deque


def num_islands(grid: List[List[str]]) -> int:

    if not grid:
        return 0

    n_islands = 0
    rows = len(grid)
    cols = len(grid[0])
    visited = set()

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        visited.add((r, c))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                r, c = dr + row, dc + col

                if (
                    r in range(rows)
                    and c in range(cols)
                    and grid[r][c] == "1"
                    and (r, c) not in visited
                ):
                    q.append((r, c))
                    visited.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                n_islands += 1
                bfs(r, c)

    return n_islands


print(
    num_islands(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1"],
        ]
    )
)


def num_islands_dfs(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    n_islands = 0
    rows = len(grid)
    cols = len(grid[0])

    def dfs(r, c):
        # base condition - Remain in the Grid
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        grid[r][c] = "0"
        # Explore 4 directions
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                n_islands += 1
                dfs(r, c) # Go deep and find all connected 1's until 0 found or end of grid

    return n_islands


print(
    num_islands_dfs(
        [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "1"], # 4x5
        ]
    )
)
