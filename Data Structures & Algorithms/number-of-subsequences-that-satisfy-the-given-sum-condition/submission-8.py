class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 1 if nums[0] * 2 <= target else 0
        nums.sort()
        l = 0
        total = 0
        r = len(nums) - 1
        while l <= r:
            if nums[r] + nums[l] > target:
                r -= 1
            else:
                gap = max(0, r - l)
                total += 2 ** gap
                l += 1

        return total % ((10 ** 9) + 7)

