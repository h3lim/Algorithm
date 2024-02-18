class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ''.join([char for char in s if char.isalnum()])
        alpha = alpha.lower()
        i = 0
        j = len(alpha) - 1

        for i in range(len(alpha) // 2):
            if alpha[i] != alpha[j]:
                return False
            j -= 1
        return True
