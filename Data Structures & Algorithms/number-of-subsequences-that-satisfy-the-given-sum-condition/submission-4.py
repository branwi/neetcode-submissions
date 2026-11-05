class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] * 2 <= target else 0
        nums.sort()
        l = 0
        total = 0
        while l < len(nums):
            for r in range(l, len(nums)):
                if nums[r] + nums[l] <= target:

                    gap = max(0, r - l - 1)
                    total += 2 ** gap
                else:
                    break
            l += 1
        return total % ((10 ** 9) + 7)

