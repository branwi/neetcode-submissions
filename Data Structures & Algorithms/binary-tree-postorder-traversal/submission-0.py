# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        stack = []
        def dfs(node):
            if not node:
                return
            stack.append(node)
            dfs(node.right)
            dfs(node.left)
            
        dfs(root)
        while stack:
            curr = stack.pop()
            postorder.append(curr.val)
        
        return postorder
            