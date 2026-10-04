class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        longest = 0
        for index, c in enumerate(s):
            if c in seen:
                c_index = seen[c]
                while l <= c_index:
                    seen.pop(s[l])
                    l+=1
                seen[c] = index
            else:
                seen[c] = index
                longest = max(index - l + 1, longest)
        return longest
                
                
