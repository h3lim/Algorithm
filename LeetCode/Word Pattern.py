class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic1 = dict()
        dic2 = dict()
        text = s.split()
        if len(pattern) != len(text):
            return False

        for i in range(len(text)):
            if pattern[i] not in dic1.keys():
                dic1[pattern[i]] = text[i]
            elif pattern[i] in dic1.keys() and dic1[pattern[i]] != text[i]:
                return False
            if text[i] not in dic2.keys():
                dic2[text[i]] = pattern[i]
            elif text[i] in dic2.keys() and dic2[text[i]] != pattern[i]:
                return False

        return True