class Solution:
    def minWindow(self, s: str, t: str) -> str:
        indices = deque([])
        need = {}
        count = {}
        met = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
            count[c] = 0
            met[c] = False
        min_len = len(s)
        ans = ""
        for i in range(len(s)):
            if s[i] in t:
                indices.append((s[i], i))
                count[s[i]] = count[s[i]] + 1
                if count[s[i]] >= need[s[i]]:
                    met[s[i]] = True
                while count[indices[0][0]] > need[indices[0][0]]:
                    count[indices[0][0]] -= 1
                    indices.popleft()
                    
                if all(met.values()) and (indices[-1][1] - indices[0][1]) < min_len:
                    min_len = indices[-1][1] - indices[0][1]
                    ans = s[indices[0][1]:indices[-1][1] + 1]
                    

        return ans
