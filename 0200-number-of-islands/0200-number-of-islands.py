class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows , cols = len(grid) , len(grid[0])
        count = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    queue = deque([(r,c)])
                    grid[r][c] = '0'

                    while queue:
                        row, col = queue.popleft()
                        for dx , dy in [(1,0), (0,1),(0,-1),(-1,0)]:
                            nx , ny = row + dx, col + dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                                queue.append((nx, ny))
                                grid[nx][ny] = '0'

                    count += 1
        return count