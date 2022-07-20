# Time: O(n^2)
# Space: O(1)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        left, right, up, down = 0, n - 1, 0, n - 1
        while count < n ** 2 + 1:
            for col in range(left, right + 1):
                ans[up][col] = count
                count += 1
            for row in range(up + 1, down + 1):
                ans[row][right] = count
                count += 1
            if up < down:
                for col in range(right - 1, left - 1, -1):
                    ans[down][col] = count
                    count += 1
            if left < right:
                for row in range(down - 1, up, -1):
                    ans[row][left] = count
                    count += 1
            left += 1
            right -= 1
            up += 1
            down -= 1
        return ans