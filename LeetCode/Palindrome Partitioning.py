from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        curr = []

        def backtrack(i):
            if i >= len(s):
                ans.append(curr.copy())
                return

            for j in range(i, len(s)):
                if self.is_palindrome(s[i:j + 1]) == True:
                    curr.append(s[i:j + 1])
                    backtrack(j + 1)
                    curr.pop()

        backtrack(0)
        return ans

    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        else:
            return False

Solution = Solution()

print(Solution.partition("aab"))