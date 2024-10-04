class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])


        def backtrack (m, n, idx):
            if idx == len(word):
                return True
            if m < 0 or m >= row or n < 0 or n >= col or board[m][n] != word[idx]:
                return False
            temp = board[m][n]
            board[m][n] = '#'


            found = (backtrack(m + 1, n, index + 1) or
                     backtrack(m - 1, n, index + 1) or
                     backtrack(m, n + 1, index + 1) or
                     backtrack(m, n - 1, index + 1))

            board[m][n] = temp
            return found
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == word [0]:
                    if backtrack(i, j, 0):
                        return True
        return False 