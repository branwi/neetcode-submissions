class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = [False] * len(nums)
        reachable[0] = True
        for i in range(len(nums)):
            if reachable[i]:
                for l in range(1, nums[i] + 1):
                    reachable[min(i + l, len(nums) - 1)] = True
        return reachable[-1]