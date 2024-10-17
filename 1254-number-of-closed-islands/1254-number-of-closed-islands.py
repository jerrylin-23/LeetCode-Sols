class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])


        def bfs(r, c):
            queue = deque([(r,c)])
            grid[r][c] = 'T'

            while queue:
                x , y = queue.popleft()

                for dx , dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx , ny = x + dx, y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                        queue.append((nx, ny))
                        grid[nx][ny] = 'T'
        count = 0 

        for i in range(cols):
            if grid[0][i] == 0:
                bfs(0 , i)
            if grid[rows - 1][i] == 0:
                bfs(rows -1 , i)

        for i in range(rows):
            if grid[i][0] == 0:
                bfs(i , 0)
            if grid[i][cols - 1] == 0:
                bfs(i , cols - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    bfs(i , j)
                    count += 1
        
        return count
            
            