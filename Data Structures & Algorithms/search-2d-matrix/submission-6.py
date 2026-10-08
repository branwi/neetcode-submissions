class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = m * n - 1
        curr = (l + r) // 2
        while l <= r:
            row = curr // n
            col = curr % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = curr - 1
                
            elif matrix[row][col] < target:
                l = curr + 1
            curr = (l + r) // 2
        return False
        
        