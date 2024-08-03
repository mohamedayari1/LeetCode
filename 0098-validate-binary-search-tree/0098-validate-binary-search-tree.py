# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.result = True

        def helper(root, left_value, right_value):
            if not root:
                return True
            if not left_value < root.val < right_value:
                return False

            self.result = (
                self.result 
                and helper(root.left, left_value, root.val)
                and helper(root.right, root.val, right_value) 
            )

            return self.result 

        return helper(root, float("-inf"), float("inf"))