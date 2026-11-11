class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        end = len(digits) - 1
        while end >= 0 and digits[end] == 9:
            digits[end] = 0
            end -= 1
        if end >= 0:
            digits[end] += 1
        if end < 0:
            ans.append(1)
        for i in range(0, end + 1):
            ans.append(digits[i])
        for i in range(end + 1, len(digits)):
            ans.append(0)
        return ans