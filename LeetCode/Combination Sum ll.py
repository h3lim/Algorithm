class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        def backtrack(curr, i):
            if sum(curr) == target:
                 ans.append(curr[:])

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if sum(curr) + candidates[j] > target:
                    break
                curr.append(candidates[j])
                backtrack(curr, j+1)
                curr.pop()

        ans = []
        backtrack([],0)
        return ans