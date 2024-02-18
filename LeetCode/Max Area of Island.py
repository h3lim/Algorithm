import queue
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        seen = set()

        def valid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1

        def bfs(r, c, val):
            q = deque([(r, c)])
            seen.add((r, c))
            while q:
                row, col = q.popleft()
                val += 1
                for dx, dy in directions:
                    nextR, nextC = row + dy, col + dx

                    if valid(nextR, nextC) and (nextR, nextC) not in seen:
                        seen.add((nextR, nextC))
                        q.append((nextR, nextC))

            return val

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1 and (i, j) not in seen:
                    val = bfs(i, j, 0)
                    ans = max(ans, val)

        return ans