# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs (root):
            if not root:
                return False
            if compare(root, subRoot):
                return True
            return dfs(root.right) or dfs(root.left)

        def compare(root, subroot):
                if not root and not subroot:
                    return True
                if not root or not subroot:
                    return False
                if root.val != subroot.val:
                    return False
                return compare(root.left, subroot.left) and compare(root.right,subroot.right)
        return dfs(root)
