# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return 
        # Implementing BFS
        queue = collections.deque([root])
        right_view = []
        while queue:
            level_length = len(queue)
            for i in range(level_length): #taking a screenshot
                current_node = queue.popleft()
                if i == level_length - 1:
                    right_view.append(current_node.val)

                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        return right_view