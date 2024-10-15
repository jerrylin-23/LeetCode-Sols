class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0 

        for i in range (rows):
            for j in range (cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    queue.append((i , j, 0))

        
        if fresh_count == 0:
            return 0
        
        while queue:

            x , y , minute = queue.popleft()
            curtime = minute

            for dx, dy in [(-1 , 0 ), (1, 0), (0, -1 ), (0, 1)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2
                    fresh_count -= 1

                    queue.append((nx , ny , minute + 1))
        
        if fresh_count > 0:
            return -1
        
        return curtime 
