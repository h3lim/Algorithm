class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        curr = 0
        while i < j:
            if (j - i) * min(height[j], height[i]) > curr:
                curr = (j - i) * min(height[j], height[i])
            if height[j] >= height[i]:
                i +=1
            else:
                j -= 1
        return curr