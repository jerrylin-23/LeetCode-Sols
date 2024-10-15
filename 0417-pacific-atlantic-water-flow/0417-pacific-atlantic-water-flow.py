class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]
    
        def bfs(start, reachable):
            queue = deque(start)
            for r, c in start:  # Mark starting points as reachable
                reachable[r][c] = True
            while queue:
                r , c =  queue.popleft()
                for dx, dy in [(1, 0), (-1 , 0), (0 , 1), (0, -1)]:
                    nx , ny  = r + dx, c + dy
                    if (0 <= nx <m and 0<= ny < n and 
                    not reachable[nx][ny] and heights[nx][ny] >= heights[r][c]):
                        reachable[nx][ny] = True
                        queue.append((nx, ny))

        pacific_starts = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        atlantic_starts =[(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        bfs(pacific_starts, pacific_reachable)
        bfs(atlantic_starts, atlantic_reachable)

        result = [[i, j] for i in range(m) for j in range(n) if atlantic_reachable[i][j] and pacific_reachable[i][j]]

        
        return result