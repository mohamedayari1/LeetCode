# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        self.result = []

        def dfs(node):
            # Preorder traversal
            if not node:
                self.result.append("N")
                return
            self.result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(self.result)
        

    def deserialize(self, data):
        vals = data.split(",")

        self.i = 0

        def dfs():
            # Preorder traversal
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            curr_node = TreeNode(int(vals[self.i]))
            self.i += 1

            curr_node.left = dfs()
            curr_node.right = dfs()

            return curr_node

        root = dfs()
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))