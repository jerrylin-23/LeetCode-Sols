class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        all_nodes = set(range(n))
        
        # Create a set of nodes with incoming edges
        nodes_with_incoming = set(y for _, y in edges)
        
        # The result is all nodes minus nodes with incoming edges
        return list(all_nodes - nodes_with_incoming)
