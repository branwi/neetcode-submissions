class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = {(1,0), (-1,0), (0,1), (0,-1)}
        queue = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
        while queue:
            row, col, d = queue.popleft()
            for rc, cc in directions:
                new_r = row + rc
                new_c = col + cc
                
                if (0 <= new_r < rows) and (0 <= new_c < cols):
                    if grid[new_r][new_c] != -1 and (d + 1 < grid[new_r][new_c]):
                        grid[new_r][new_c] = d + 1
                        queue.append((new_r, new_c, d + 1))

        
        
