from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        sol = 0
        maxf = 0
        chars = defaultdict(int)

        while r < len(s):
            chars[s[r]] += 1
            maxf = max(maxf, chars[s[r]])

            wsize = r - l + 1

            while (wsize - maxf) > k:
                chars[s[l]] -= 1
                l += 1
                wsize = r - l + 1

            sol = max(wsize, sol)
            r += 1

        return sol