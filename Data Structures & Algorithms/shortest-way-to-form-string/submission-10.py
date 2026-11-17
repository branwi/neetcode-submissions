class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sp = 0
        count = 1
        for c in target:
            if c not in source:
                return -1
            while sp < len(source) and source[sp] != c:
                sp += 1
            
            if sp == len(source):
                count += 1
                sp = source.index(c)
            sp += 1
        return count
