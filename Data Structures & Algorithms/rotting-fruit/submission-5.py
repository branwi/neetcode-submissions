class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        sol = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        while queue:
            row, col, time = queue.popleft()
            sol = max(time, sol)
            for d in directions:
                cr, cc = d
                new_r, new_c = row + cr, col + cc
                if 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    queue.append((new_r, new_c, time + 1))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
                    
        return sol