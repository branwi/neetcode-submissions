class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l = 0
        r = n
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        for c in s1:
            s1_dict[c] += 1
        for c in s2[0:n]:
            s2_dict[c] += 1
        print(s1_dict)
        print(s2_dict)
        while r < len(s2):
            if s1_dict == s2_dict:
                return True
            s2_dict[s2[l]] -= 1
            if s2_dict[s2[l]] == 0:
                s2_dict.pop(s2[l])
            s2_dict[s2[r]] += 1
            print(s2_dict)
            r += 1
            l += 1
        if s1_dict == s2_dict:
                return True
        return False
            
