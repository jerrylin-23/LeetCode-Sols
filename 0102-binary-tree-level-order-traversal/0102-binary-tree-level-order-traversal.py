# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result  = []

        queue = deque([root])

        while queue:
            current_level = []
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.popleft()
                current_level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            result.append(current_level)
        
        return result