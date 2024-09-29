class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_board_value (idx):
            r = (idx - 1) // n
            c = (idx - 1) % n
            if r % 2 == 0:
                return board[n - 1 -r][c]
            else: 
                return board [n - 1- r][n - 1 -c]
            
        visited = set()
        queue = deque([(1,0)])
        visited.add(1)

        while queue:
            curr, moves = queue.popleft()

            if curr == n*n:
                return moves
            for next_square in range ( curr + 1, min (curr + 6 ,n * n) + 1):
                board_value = get_board_value(next_square)
                if board_value != -1:
                    next_square = board_value
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1

