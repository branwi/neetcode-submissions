class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        paths = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def memo(r, c):
            if (r, c) in paths:
                return paths[(r, c)]
            for rc, cc in directions:
                new_r = rc + r
                new_c = cc + c
                if (0 <= new_r < row) and (0 <= new_c < col):
                    if (matrix[r][c] > matrix[new_r][new_c]):
                        
                        paths[(r, c)] = max(paths.get((r, c), 0), 1 + memo(new_r, new_c))
            if not paths.get((r, c), 0):
                paths[(r, c)] = 1
            return paths[(r, c)]
        ans = -1
        for i in range(row):
            for j in range(col):
                ans = max(ans, memo(i, j))
        return ans
            