# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: 
            return False
        stack = [(root, targetSum)]

        while stack: 
            node, currentSum = stack.pop()
            if not node.right and not node.left and node.val ==  currentSum:
                return True 

            if node.right:
                stack.append((node.right, currentSum - node.val))
            if node.left:
                stack.append((node.left, currentSum - node.val))
            
        return False