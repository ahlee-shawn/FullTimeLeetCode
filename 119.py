# Time: O(n^2)
# Space: O(1)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        ans = [1, 1]
        for i in range(2, rowIndex + 1):
            ans.append(1)
            for j in range(i - 1, 0, -1):
                ans[j] = ans[j] + ans[j-1]
        return ans