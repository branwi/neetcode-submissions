class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        curr = (l + r) // 2
        while l <= r:
            if nums[curr] == target:
                return curr
            elif nums[curr] > target:
                r = curr - 1
                curr = (l + r) // 2
            elif nums[curr] < target:
                l = curr + 1
                curr = (l + r) // 2
        return -1