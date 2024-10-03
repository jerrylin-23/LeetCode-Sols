# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_depth = 0 

        def dfs(node: TreeNode) -> int:
            if not node: 
                return 0
            

            left_height = dfs(node.right)
            right_height = dfs(node.left)

            self.max_depth = max (self.max_depth, left_height + right_height)

            return max (left_height, right_height) + 1

        dfs (root)
        return self.max_depth 