# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return
        val_arr = []
        def collect(node):
            if node is None:
                return
            else:
                val_arr.append(node.val)
            collect(node.right)
            collect(node.left)

        collect(root)
        val_arr.sort()

        return val_arr[k - 1]
