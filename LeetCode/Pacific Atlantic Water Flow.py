import queue
from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            pointX, pointY = r, c
            seen = set()
            q = deque([(r, c)])
            seen.add((r, c))
            pacific = 0
            atlantic = 0

            while q:
                row, col = q.popleft()
                if row == 0 or col == 0:
                    pacific = 1
                if row == m - 1 or col == n - 1:
                    atlantic = 1
                if pacific == 1 and atlantic == 1:
                    return (pointX, pointY)

                for dx, dy in directions:
                    nextR, nextC = row + dy, col + dx
                    if 0 <= nextR < m and 0 <= nextC < n and (nextR, nextC) not in seen and heights[nextR][nextC] <= \
                            heights[row][col]:
                        seen.add((nextR, nextC))
                        q.append((nextR, nextC))

            return (-1, -1)

        ans = []

        for i in range(m):
            for j in range(n):
                x, y = bfs(i, j)
                if (x, y) != (-1, -1):
                    ans.append([x, y])

        return ans
Solution = Solution()

print(Solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
