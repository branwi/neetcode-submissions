class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = {}
        count = {}
        met = {}

        for c in t:
            need[c] = need.get(c, 0) + 1
            count[c] = 0
            met[c] = False

        left = 0
        min_len = len(s) + 1
        ans = ""

        for right in range(len(s)):
            if s[right] in need:
                count[s[right]] += 1

                if count[s[right]] >= need[s[right]]:
                    met[s[right]] = True

                while left <= right and (s[left] not in need or count[s[left]] > need[s[left]]):
                    if s[left] in need:
                        count[s[left]] -= 1
                    left += 1

                if all(met.values()) and (right - left + 1) < min_len:
                    min_len = right - left + 1
                    ans = s[left:right + 1]

        return ans