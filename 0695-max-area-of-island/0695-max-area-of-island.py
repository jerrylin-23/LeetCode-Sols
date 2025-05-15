class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows , cols = len(grid), len(grid[0])
        max_island = 0
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue = deque ([(r, c)])
                    grid[r][c] = 0
                    
                    counter = 1
                    while queue:
                        dx, dy = queue.popleft()
                        for dr, dw in [(0,1), (1,0), (0,-1),(-1,0)]:
                            nx , ny = dx + dr, dy + dw
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                                counter += 1
                                queue.append((nx, ny))
                                grid[nx][ny] = 0
                    max_island = max(max_island, counter)
        return max_island
                        
                        
