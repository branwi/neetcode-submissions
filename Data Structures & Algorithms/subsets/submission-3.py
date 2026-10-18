class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        sol = []
        
        def generate_subset(index, curr):
            nonlocal sol
            if index == len(nums):
                sol.append(curr)
                return None
            generate_subset(index + 1, curr)
            generate_subset(index + 1, curr + [nums[index]])

        generate_subset(0, [])
        return sol