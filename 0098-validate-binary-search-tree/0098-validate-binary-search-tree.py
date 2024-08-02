# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, left_value, right_value):
            
            if not node:
                return True
            
            if not (left_value < node.val < right_value):
                return False
            
            return (
                helper(node.left, left_value, node.val) and 
                helper(node.right, node.val, right_value)
            )
        return helper(root, float("-inf"), float("inf"))