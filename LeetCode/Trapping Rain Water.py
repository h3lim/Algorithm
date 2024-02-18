class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if leftMax <= rightMax:
                left += 1
                if leftMax - height[left] > 0:
                    ans += leftMax - height[left]
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                if rightMax - height[right] > 0:
                    ans += rightMax - height[right]
                rightMax = max(rightMax, height[right])

        return ans


