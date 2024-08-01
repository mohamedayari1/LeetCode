# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def encoder(self, root: Optional[TreeNode]) -> str:
        result = []
        self.i = 0

        def helper(node):
            if not node:
                self.i += 1
                result.append('N')
                return 
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return ','.join(result)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_string = self.encoder(p)
        q_string = self.encoder(q)
        
        return p_string ==  q_string