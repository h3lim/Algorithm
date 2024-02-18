from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        counter = Counter()
        for right in range(len(s)):
            counter[s[right]] += 1
            key, value = counter.most_common(1)[0]
            while sum(counter.values()) - value > k:
                counter[s[left]] -= 1
                left += 1
                key, value = counter.most_common(1)[0]
            print(counter)
            ans = max(ans, right - left + 1)

        return ans

Solution = Solution()

Solution.characterReplacement("AABABBA", 1)