class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        total = 1
        without_zero = 0
        l = []
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                total = total * n
        if zero_count == 1:
            without_zero = total

        if zero_count > 0:
            total = 0
        
        for n in nums:
            if n == 0:
                l.append(without_zero)
            else:
                l.append(int(total / n))
        return l