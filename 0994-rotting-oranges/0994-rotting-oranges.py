class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1 
        rows, cols = len(grid) , len(grid[0])
        time = 0
        fresh_count = 0
        queue = deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) 
                if grid[r][c] == 1:
                    fresh_count += 1

                    
              
              
        while queue:
            row , col, cur_time = queue.popleft()
            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                nx , ny = dx + row , dy + col
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    queue.append((nx, ny, cur_time + 1))
                    grid[nx][ny] = 2
                    fresh_count -= 1
                    time = cur_time + 1

        return -1 if fresh_count else time
                
        
                        