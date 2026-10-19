class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        def dfs(combos, curr):
            
            if curr == target:
                sol.append(combos)
                return
            elif curr > target:
                return
            else:
                for num in nums:
                    if not combos or num >= combos[-1]:
                        dfs(combos + [num], curr + num)
        
        dfs([], 0)
        return sol