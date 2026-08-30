from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = defaultdict(int)
        chars_t = defaultdict(int)

        for char in s:
            chars_s[char] += 1

        for char in t:
            chars_t[char] += 1

        return chars_s == chars_t