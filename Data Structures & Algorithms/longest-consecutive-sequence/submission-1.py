class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start_nums = []
        for n in nums:
            if (n - 1) not in nums_set:
                start_nums.append(n)
        max_length = 0
        
        for n in start_nums:
            l = 1
            start = n
            while (start + 1) in nums_set:
                start = start + 1
                l += 1
            
            max_length = max(max_length, l)
        
        return max_length

        