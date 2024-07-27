# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _find_preorder_and_inorder(self, preorder: List[int], inorder: List[int]) -> Tuple[Tuple[List[int], List[int]], Tuple[List[int], List[int]]]:
        """ Finds the inorder and preorder lists of the left and right subtrees. """
        root_val = preorder[0]

        i = inorder.index(root_val)

        left_inorder = inorder[:i]
        right_inorder = inorder[i+1:]

        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[len(left_inorder)+1:]

        left_lists = (left_preorder, left_inorder)
        right_lists = (right_preorder, right_inorder)
        return left_lists, right_lists

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root_val = preorder[0]
        root_node = TreeNode(root_val)

        left_lists, right_lists = self._find_preorder_and_inorder(preorder, inorder)
        left_preorder, left_inorder = left_lists
        right_preorder, right_inorder = right_lists

        root_node.left = self.buildTree(left_preorder, left_inorder)
        root_node.right = self.buildTree(right_preorder, right_inorder)

        return root_node
