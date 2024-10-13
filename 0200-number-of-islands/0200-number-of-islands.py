
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, col = len(grid), len(grid[0])
        num_islands = 0

        def bfs(r, c):
            queue = deque([(r, c)])
            grid[r][c] = "0"

            while queue:
                x, y = queue.popleft()

                # Visit all four neighbors (up, down, left, right)
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy

                    # Check if the neighbor is in bounds and is land ('1')
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                        grid[nx][ny] = "0"  # Mark as visited
                        queue.append((nx, ny))

    # Loop over the entire grid
        for i in range(rows):
            for j in range(col):
                if grid[i][j] == "1":  # Found an island
                    num_islands += 1
                    bfs(i, j)  # Explore the entire island

        return num_islands
