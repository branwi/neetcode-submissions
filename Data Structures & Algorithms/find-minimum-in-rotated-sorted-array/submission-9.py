class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        curr = (l + r) // 2
        while l < r:
            if nums[curr] > nums[r]:
                l = curr + 1
            else:
                r = curr
            curr = (l + r) // 2
        return nums[l]