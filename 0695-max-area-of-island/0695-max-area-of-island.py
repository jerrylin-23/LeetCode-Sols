class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0
        rows = len(grid)
        cols = len(grid[0])
        max_island_area = 0

        def bfs(r, c):
            queue =  deque([(r , c)])
            grid[r][c] = 0
            island_area = 1

            while queue:
                x , y = queue.popleft()
                

                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        queue.append((nx, ny))
                        island_area += 1
            return island_area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_island_area = max(max_island_area , bfs (i , j))
        
        return max_island_area