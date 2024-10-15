class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 

        m , n = len(board),  len(board[0])

        def bfs (start):
            queue = deque([start])
            r, c  = start
            board[r][c] = 'T'

            while queue:
                r, c =  queue.popleft()
                for dx, dy in [(1 , 0), (-1, 0), (0, 1 ), (0 ,-1)]:
                    nx , ny = dx + r, dy + c
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                        board[nx][ny] = 'T'
                        queue.append((nx, ny))
        for i in range(m):
            if board[i][0] == 'O':
                bfs((i, 0))
            if board[i][n - 1] == 'O':
                bfs((i, n - 1))
        for j in range(n):
            if board[0][j] == 'O':
                bfs((0, j))
            if board[m - 1][j] == 'O':
                bfs((m - 1, j))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'

        


        