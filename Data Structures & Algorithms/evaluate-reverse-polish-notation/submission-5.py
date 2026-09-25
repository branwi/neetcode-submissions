class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens.pop())
        tokens.reverse()
        stack = []
        stack.append(int(tokens.pop()))
        stack.append(int(tokens.pop()))
        while tokens:
            op = tokens.pop()
            if op == '+': 
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
            elif op == '*':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 * n2)
            elif op == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif op == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(op))
        
        return stack.pop()

        