# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_same_tree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
        if not p and not q:
            return True 
        if not p or not q:
            return False
        return (p.val == q.val 
                and self.is_same_tree(p.left, q.left)  
                and self.is_same_tree(p.right, q.right))


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Implementing BFS
        if not subRoot:
            return True
        if not root:
            return False 

        is_subtree = False
        queue = collections.deque([root])

        while queue and not is_subtree:
            for i in range(len(queue)):
                
                curr_node = queue.popleft()
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

                is_subtree = self.is_same_tree(curr_node, subRoot)
                if is_subtree:
                    break

        return is_subtree
