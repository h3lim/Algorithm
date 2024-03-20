class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        def countNeighbor(i, j):
            neighbor = 0
            for r in range(i - 1, i + 2):
                for c in range(j - 1, j + 2):
                    if ((r == i) and (c == j)) or r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                        continue
                    elif board[r][c] == 1 or board[r][c] == 3:
                        neighbor += 1

            return neighbor

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = countNeighbor(i, j)
                if board[i][j] == 0 and num == 3:
                    board[i][j] = 2
                if board[i][j] == 1:
                    if num in [2, 3]:
                        board[i][j] = 3
                    else:
                        board[i][j] = 1

        # 0 0 0
        # 1 0 1
        # 0 1 2
        # 1 1 3
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 1







