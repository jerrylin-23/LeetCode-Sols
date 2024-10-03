# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
    
        def same_tree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            
            return same_tree(n1.left, n2.left) and same_tree(n1.right, n2.right)
        
        if root.val == subRoot.val:
            if same_tree(root, subRoot):
                return True
         
        return self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot)