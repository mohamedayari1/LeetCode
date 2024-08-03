# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def helper(self, preorder: List[int], inorder: List[int]) -> Tuple[Tuple[List[int], List[int]], Tuple[List[int], List[int]]]:
        
        root = preorder[0]
        index = inorder.index(root)

        left_inorder, right_inorder = inorder[:index], inorder[index + 1:]
        left_preorder, right_preorder = preorder[1:len(left_inorder) + 1], preorder[len(left_inorder)+1:]

        left_lists  = (left_preorder, left_inorder)
        right_lists  = (right_preorder, right_inorder)

        return left_lists, right_lists

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None


        root_value = preorder[0]
        root_node  = TreeNode(root_value)

        left_lists, right_lists = self.helper(preorder, inorder)

        root_node.left = self.buildTree(left_lists[0], left_lists[1])
        root_node.right = self.buildTree(right_lists[0], right_lists[1])

        return root_node

        