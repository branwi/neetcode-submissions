class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if count:
                    return False

                count = True
                cannot_lower_left = i > 0 and nums[i - 1] > nums[i + 1]
                cannot_raise_right = i + 2 < len(nums) and nums[i] > nums[i + 2]

                if cannot_lower_left and cannot_raise_right:
                    return False
        return True