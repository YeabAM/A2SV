# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            return dfs(node1.right, node2.left) and dfs(node1.left, node2.right)
        
        return dfs(root.left, root.right)
        
