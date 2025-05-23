class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        queue = deque()
        
        for r in range(m):
            if board[r][0] == 'O':
                queue.append((r,0))
            if board[r][n-1] == 'O':
                queue.append((r,n-1))
        for c in range(n):
            if board[0][c] == 'O':
                queue.append((0,c)) 
            if board[m-1][c] == 'O':
                queue.append((m-1, c))
           
        

        while queue:
            row, col = queue.popleft()
            if 0 <= row < m and 0 <= col < n and board[row][col] == 'O':
                board[row][col] = 'S'
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = dx + row, dy + col
                    queue.append((nx, ny))


        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'S':
                    board[r][c] ='O'