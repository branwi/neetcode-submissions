class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined_list = []
        for l in matrix:
            combined_list.extend(l)
        
        l = 0
        r = len(combined_list) - 1
        curr = (l + r) // 2
        while l <= r:
            if combined_list[curr] == target:
                return True
            elif combined_list[curr] > target:
                r = curr - 1
                curr = (l + r) // 2
            elif combined_list[curr] < target:
                l = curr + 1
                curr = (l + r) // 2
        return False
        
        