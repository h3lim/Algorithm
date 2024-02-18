from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            seen = set()
            region = set()

            region.add((r, c))
            q = deque([(r, c)])
            seen.add((r, c))
            while q:
                row, col = q.popleft()

                for dx, dy in directions:
                    nextR, nextC = row + dy, col + dx

                    if (0 <= nextR < len(board)) and (0 <= nextC < len(board[0])) and (nextR, nextC) not in seen and board[nextR][nextC] == 'O':
                        region.add((nextR, nextC))
                        seen.add((nextR, nextC))
                        q.append((nextR, nextC))

            for x, y in region:
                if x == 0 or x == len(board) - 1 or y == 0 or y == len(board[0]) - 1:
                    return

            for x, y in region:
                board[x][y] = "X"
            return

        for i in range(len(board)):
            for j in range(len(board[i])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[i]) - 1:
                    continue
                if board[i][j] == "O":
                    bfs(i, j)

Solution = Solution()

print(Solution.solve([["O","O","O"],["O","O","O"],["O","O","O"]]))
