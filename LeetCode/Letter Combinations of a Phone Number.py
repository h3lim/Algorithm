from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        DIC = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        if len(digits) == 0:
            return []
        def backtrack(curr,i):
            if len(curr) >= len(digits):
                s = "".join(curr)
                ans.append(s)
                return

            for j in range(len(DIC[int(digits[i])])):
                s = DIC[int(digits[i])]
                curr.append(s[j])
                backtrack(curr, i+1)
                curr.pop()

        ans = []
        backtrack([],0)
        return ans

Solution = Solution()

print(Solution.letterCombinations("23"))
