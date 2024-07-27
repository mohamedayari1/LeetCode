# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.result = 0
        
        
        def preorder_dfs(node, max_value):
            if not node:
                return 0
            
            #Implementing preorder dfs
            self.result = 1 if node.val >= max_value else 0
            max_value = max(max_value, node.val)
            
            self.result += preorder_dfs(node.left, max_value) + preorder_dfs(node.right, max_value)
            
            return self.result 

        self.result = preorder_dfs(root, root.val)
        return self.result