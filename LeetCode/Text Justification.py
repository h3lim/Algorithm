import collections
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        line = []
        length = 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                space = maxWidth - length
                quotient = space // max(1, len(line) - 1)
                remainder = space % max(1, len(line) - 1)
                for j in range(max(1, len(line) -1)):
                    line[j] += " " * quotient
                    if remainder:
                        line[j] += " "
                        remainder -= 1
                ans.append("".join(line))
                line, length = [], 0

            line.append(words[i])
            length = length + len(words[i])
            i = i + 1

        last_line = " ".join(line)
        trail_space = maxWidth - len(last_line)
        ans.append(last_line + " " * trail_space)
        return ans

solution = Solution()
words = ["This", "is", "an", "example", "of", "text", "justification"]
maxWidth = 16
ans = []

ans = solution.fullJustify(words,maxWidth)







