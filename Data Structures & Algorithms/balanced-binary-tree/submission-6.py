# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def subtree(root, depth):
            if not root:
                return depth - 1
            
            return max(subtree(root.right, depth + 1), subtree(root.left, depth + 1))
        if not root:
            return True
        def valid(root):
            if not root:
                return True
            left = subtree(root.left, 1)
            right = subtree(root.right, 1)
            return abs(left-right) <= 1
        
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                if not valid(node):
                    return False


        return True

            