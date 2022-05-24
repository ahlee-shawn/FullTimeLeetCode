# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            ans = max(ans, width * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans