"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clone = {node: Node(node.val)}
        queue =  deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                clone[curr].neighbors.append(clone[neighbor])
        return clone[node]

