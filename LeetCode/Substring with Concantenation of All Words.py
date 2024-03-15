from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []
        dic = dict()
        left = 0
        length = 0
        sLen = len(words[0])
        for i in words:
            dic[i] = 1

        # bar foo foo bar the foo bar man
        # cnt = 2
        for right in range(0, len(s), sLen):
            if s[right:right + sLen] in dic.keys():
                dic[s[right:right + sLen]] = dic[s[right:right + sLen]] - 1
            length += 1

            while length > len(words):
                if s[left:left + sLen] in dic.keys():
                    dic[s[left:left + sLen]] += 1
                length -= 1
                left += sLen

            if all(val == 0 for val in dic.values()):
                ans.append(left)

        return ans

Solution = Solution()


print(Solution.findSubstring("barfoofoobarthefoobarman", words = ["bar","foo","the"]))
