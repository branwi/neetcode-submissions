class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            left = target - nums[i]
            if left in prev:
                return [prev[left], i]
            
            prev[nums[i]] = i
        return[]
