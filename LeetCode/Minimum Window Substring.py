class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt, window = {}, {}

        for c in t:
            cnt[c] = 1 + cnt.get(c, 0)

        have, need = 0, len(cnt)
        ans, ansLen = [0,0], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in cnt and window[c] == cnt[c]:
                have += 1

            while have == need:
                if (r - l + 1) < ansLen:
                    ans = [l, r]
                    ansLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in cnt and window[s[l]] < cnt[s[l]]:
                    have -= 1
                l += 1
        l, r = ans
        return s[l:r+1] if ansLen != float("inf") else ""

Solution = Solution()

print(Solution.minWindow("ADOBECODEBANC", "ABC"))
