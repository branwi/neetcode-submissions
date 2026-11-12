class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        left_sum = 0
        right_sum = 0
        for i in range(right + 1):
            if i < left:
                left_sum += self.nums[i]
            right_sum += self.nums[i]
        
        return right_sum - left_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)