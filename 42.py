# Time: O(n)
# Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        while left < right:
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    ans += (leftMax - height[left])
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    ans += (rightMax - height[right])
                right -= 1
        return ans