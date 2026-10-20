class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)
        ]
        queue = deque([(0, 0, 1)])
        visited = set()
        while queue:
            r, c, total = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return total
            else:
                for cr, cy in directions:
                    new_r, new_c = r + cr, c + cy
                    if (new_r, new_c) not in visited and 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 0:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c, total + 1))
        return -1