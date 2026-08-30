class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = {}
        for index, num in enumerate(nums):
            i[num] = index
        for index, num in enumerate(nums):
            diff = target - num
            if diff in i and i[diff] != index:
                return [index, i[diff]]
        
        return []