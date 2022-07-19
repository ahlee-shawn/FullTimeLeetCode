# Time: O(n)
# Space: O(n)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                ans = max(ans, cur_height * cur_width)
            stack.append(i)
            
        while stack[-1] != -1:
            cur_height = heights[stack.pop()]
            cur_width = len(heights) - stack[-1] - 1
            ans = max(ans, cur_height * cur_width)
        return ans