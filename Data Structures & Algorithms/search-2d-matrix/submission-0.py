class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        combined_list = []
        for l in matrix:
            combined_list.extend(l)
        
        l = 0
        r = len(combined_list) - 1
        while l <= r:
            curr = (l + r) // 2
            if combined_list[curr] == target:
                return True
            elif combined_list[curr] > target:
                r = curr - 1
            else:
                l = curr + 1
        
        return False
        
        