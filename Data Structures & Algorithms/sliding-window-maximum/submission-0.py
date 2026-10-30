class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_n = -10001
        max_i = 0
        for i in range(0, k):
            if nums[i] >= max_n:
                max_n = nums[i]
                max_i = i
        result = []
        left = 0
        result.append(max_n)
        for right in range(k, len(nums)):
            left += 1
            if nums[right] > max_n:
                max_i = right
                max_n = nums[right]
            elif left > max_i:
                max_n = -10001
                for i in range(left, right + 1):
                    if nums[i] >= max_n:
                        max_n = nums[i]
                        max_i = i
            result.append(max_n)
        return result
