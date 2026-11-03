# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val == root2.val:
                return sameTree(root1.left, root2.left) and sameTree(root1.right, root2.right)
            else:
                return False
        
        def dfs(node):
            if not node:
                return False

            return (
                sameTree(node, subRoot)
                or dfs(node.left)
                or dfs(node.right)
            )

        # An empty tree is a subtree of any tree.
        if not subRoot:
            return True

        return dfs(root)