class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        j = len(nums) - k
        l = nums[0:j]
        r = nums[j:]
        r.extend(l)
        print(r)
        nums[:] = r