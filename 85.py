# Time: O(m*n)
# Space: O(n)
class Solution:
    def helper(self, matrix):
        result = 0
        stack = [-1]
        for i in range(len(matrix)):
            while stack[-1] != -1 and matrix[stack[-1]] > matrix[i]:
                cur_height = matrix[stack.pop()]
                cur_width = i - stack[-1] - 1
                result = max(result, cur_height * cur_width)
            stack.append(i)
        while stack[-1] != -1:
            cur_height = matrix[stack.pop()]
            cur_width = len(matrix) - stack[-1] - 1
            result = max(result, cur_height * cur_width)
        return result
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        m, n = len(matrix), len(matrix[0])
        dp = [0 for _ in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[j] += 1
                else:
                    dp[j] = 0
            ans = max(ans, self.helper(dp))
        return ans