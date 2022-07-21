# Time: O(m * n)
# Space: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_has_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_has_zero = True
                break
        for i in range(1, m):
            row_has_zero = False
            for j in range(n):
                if matrix[i][j] == 0:
                    row_has_zero = True
                    matrix[0][j] = 0
            if row_has_zero:
                for k in range(n):
                    matrix[i][k] = 0
        for j in range(n):
            if matrix[0][j] == 0 and m > 1:
                for i in range(m):
                    matrix[i][j] = 0
        if first_has_zero:
            for k in range(n):
                matrix[0][k] = 0