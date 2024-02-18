from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        seen = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def valid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and int(grid[row][col]) == 1

        def bfs(r, c):
            q = deque([(r, c)])

            while q:
                row, col = q.popleft()
                for dx, dy in directions:
                    nextR, nextC = row + dy, col + dx
                    if valid(nextR, nextC) and (nextR, nextC) not in seen:
                        seen.add((nextR, nextC))
                        q.append((nextR, nextC))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in seen and int(grid[i][j]) == 1:
                    ans += 1
                    bfs(i, j)

        return ans

Solution = Solution()

print(Solution.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))