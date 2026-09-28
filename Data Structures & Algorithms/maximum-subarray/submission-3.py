class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = float("-inf")
        min_sum = float("inf")
        total = 0
        max_num = float("-inf")
        for num in nums:
            total += num
            min_sum = min(min_sum, total)
            max_sum = max(max_sum, total)
            max_num = max(max_num, num)
        
        if min_sum > 0:
            min_sum = 0
        if max_num < 0:
            return max_num
        return max_sum - min_sum
        