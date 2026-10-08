class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_dict = {}
        for index, num in enumerate(nums):
            nums_dict[num] = index
        
        nums.sort()
        l = 0
        r = len(nums) - 1
        curr = (l + r) // 2
        while l <= r:
            if nums[curr] == target:
                return nums_dict[nums[curr]]
            elif nums[curr] > target:
                r = curr - 1
                curr = (l + r) // 2
            elif nums[curr] < target:
                l = curr + 1
                curr = (l + r) // 2
        return -1