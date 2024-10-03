# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def balance(node: TreeNode) -> int:
            if not node:
                return 0 
            left_height = balance(node.right)
            right_height = balance(node.left)

            if left_height == -1 or right_height == -1 or abs (left_height - right_height) > 1:
                return -1 
            
            return max(left_height, right_height) + 1
        

        return balance(root) != -1 