# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque([root])
        result = []
        while queue:
            list_of_curr_lvl = []
            for i in range(len(queue)):
                curr_node = queue.popleft()
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right) 
                list_of_curr_lvl.append(curr_node.val)
            result.append(list_of_curr_lvl)
        
        return result