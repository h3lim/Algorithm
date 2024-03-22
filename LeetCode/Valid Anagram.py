class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = list(s)
        t1 = list(t)

        s1.sort()
        t1.sort()

        if s1 == t1:
            return True
        else:
            return False