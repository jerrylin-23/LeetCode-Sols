class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n 

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(x,y):
            root1, root2 = find(x), find(y)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root2] > rank[root1]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
        
        for start, end in edges:
            union(start, end)
        
        return find(source) == find(destination)
                


