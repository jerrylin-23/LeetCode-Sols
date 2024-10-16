class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)] 
        rank = [1] * n  

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])  
            return parent[node]


        def union(node1, node2):
            root1 = find(node1)
            root2 = find(node2)

            if root1 != root2:  
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j:
                    union(i, j)

        provinces =set(find(i) for i in range(n))
        return len(provinces)
