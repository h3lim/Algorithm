from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        s = set()
        for i in triplets:
            if i[0] > target[0] or i[1] > target[1] or i[2] > target[2]:
                continue

            for j, v in enumerate(i):
                if v == target[j]:
                    s.add(j)

        return len(s) == 3

Solution = Solution()

print(Solution.mergeTriplets(triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]))

