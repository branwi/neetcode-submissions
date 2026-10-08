class Solution:
    def findMin(self, nums: List[int]) -> int:
        f = nums[0]
        l = 0
        r = len(nums) - 1
        curr = 0
        while l < r:
            curr = (l + r) // 2
            if nums[curr] > nums[l]:
                l = curr
            else:
                r = curr
        
        return min(nums[(curr + 1) % len(nums)], f)
