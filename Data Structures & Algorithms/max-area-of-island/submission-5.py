class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        total = 0
        def dfs(row, col):
            nonlocal count
            grid[row][col] = 0
            for d in directions:
                r, c = d
                new_r, new_c = row + r, col + c
                if new_r < ROWS and new_r >= 0 and new_c < COLS and new_c >= 0 and grid[new_r][new_c] == 1:
                    count += 1
                    dfs(new_r, new_c)
            return
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    count = 1
                    dfs(r, c)
                    total = max(total, count)
        return total