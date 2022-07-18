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

# Time: O(n)
# Space: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i - 1])
        right[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            right[i] = max(height[i], right[i + 1])
        ans = 0
        for i in range(len(height)):
            ans += (min(left[i], right[i]) - height[i])
        return ans