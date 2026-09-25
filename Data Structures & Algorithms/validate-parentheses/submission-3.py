class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        pairs = {'(': ')', '{': '}', '[': ']'}
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack:
                    return False
                if c != pairs[stack.pop()]:
                    return False
        return len(stack) == 0
                
