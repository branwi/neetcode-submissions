class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        min_len = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            if total >= target:
                min_len = min(r - l + 1, min_len)
            while total - nums[l] >= target and l < r:
                total -= nums[l]
                l += 1
                min_len = min(r - l + 1, min_len)


        if min_len == len(nums) + 1:
            return 0
        return min_len
