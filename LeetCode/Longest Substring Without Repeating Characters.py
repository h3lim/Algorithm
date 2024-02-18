class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        l = []
        for right in range(len(s)):
            l.append(s[right])
            while len(l) != len(set(l)):
                    l.remove(s[left])
                    left+=1
            ans = max(ans, len(l))
        return ans
