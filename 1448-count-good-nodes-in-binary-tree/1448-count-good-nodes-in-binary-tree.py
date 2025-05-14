# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0 
        queue = deque([(root, root.val)])

        while queue: 
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                count += 1

            new_max = max(node.val, max_so_far) 

            if node.left:
                queue.append((node.left, new_max))

            if node.right:
                queue.append((node.right, new_max))
        
        return count
            