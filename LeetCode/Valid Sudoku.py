from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(9):
                if board[i][j] != ".":
                    row[int(board[i][j])] = row[int(board[i][j])] + 1
                if 2 in row:
                    return False

        for i in range(9):
            col = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(9):
                if board[j][i] != ".":
                    col[int(board[j][i])] = col[int(board[j][i])] + 1
                if 2 in col:
                    return False

        for i in range(9):
            smallSqr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            num = 0
            if i < 3:
                num = 0
            elif i < 6:
                num = 3
            else:
                num = 6
            for j in range(3):
                for k in range(3):
                    print(j + num, k + ((i * 3) % 9))
                    if board[j+num][k+((i*3)%9)] != ".":
                        smallSqr[int(board[j + num][k+((i*3)%9)])] = smallSqr[int(board[j + num][k+((i*3)%9)])] + 1
                    if 2 in smallSqr:
                        return False
        return True


Solution = Solution()
board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
res = Solution.isValidSudoku(board)

print(res)
