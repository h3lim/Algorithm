from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {i : [] for i in range(numCourses)}

        for c, p in prerequisites:
            map[c].append(p)

        visited = set()

        def dfs(c):
            if c in visited:
                return False
            if map[c] == []:
                return True

            visited.add(c)

            for p in map[c]:
                if not dfs(p): return False
            visited.remove(c)
            map[c] = []
            return True

        for c in range(numCourses):
            if not dfs(c): return False
        return True


Solution = Solution()

print(Solution.canFinish(6,[[2,1],[3,1],[2,3],[4,2],[5,4]]))