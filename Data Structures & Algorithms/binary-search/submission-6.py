class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            start = (l + r) // 2
            if nums[start] == target:
                return start
            elif nums[start] > target:
                r = start - 1
            else:
                l = start + 1
        return -1
        