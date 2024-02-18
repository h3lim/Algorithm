from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        t, freshOrg = 0, 0
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    freshOrg += 1
                if  grid[i][j] == 2:
                    q.append([i,j])

        while q and freshOrg > 0:
            for o in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    nextRow, nextCol = row + dr, col + dc

                    if nextRow < 0 or nextRow == ROWS or nextCol < 0 or nextCol == COLS or grid[nextRow][nextCol] != 1:
                        continue

                    grid[nextRow][nextCol] = 2
                    q.append([nextRow,nextCol])
                    freshOrg -= 1
            t += 1

        return t if freshOrg == 0 else -1


Solution = Solution()

print(Solution.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))