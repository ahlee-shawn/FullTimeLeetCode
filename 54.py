# Time: O(m * n)
# Space: O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []
        count = 0
        up, down, left, right = 0, m - 1, 0, n - 1
        while len(ans) < m * n:
            for col in range(left, right + 1):
                ans.append(matrix[up][col])
            for row in range(up + 1, down + 1):
                ans.append(matrix[row][right])
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[down][col])
            if left != right:
                for row in range(down - 1, up, -1):
                    ans.append(matrix[row][left])
            up += 1
            down -= 1
            left += 1
            right -= 1
        return ans