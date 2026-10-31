# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_stack = [q]
        p_stack = [p]
        while q_stack and p_stack:
            q_node = q_stack.pop()
            p_node = p_stack.pop()
            
            if q_node or p_node:
                if not (q_node and p_node):
                    return False
                else:
                    if q_node.val != p_node.val:
                        return False
                    q_stack.append(q_node.left)
                    q_stack.append(q_node.right)
                    p_stack.append(p_node.left)
                    p_stack.append(p_node.right)

        if q_stack or p_stack:
            return False
        return True