# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.result = True

        def helper(root):
            if not root:
                return 0
            left, right = helper(root.left), helper(root.right)

            self.result = abs(left - right) <= 1 and self.result

            return 1 + max(left, right)
        helper(root)
        return self.result