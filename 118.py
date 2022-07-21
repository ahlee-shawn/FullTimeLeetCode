# Time: O(n^2)
# Space: O(1)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows >= 1:
            ans.append([1])
        if numRows >= 2:
            ans.append([1,1])
        for i in range(3, numRows + 1):
            prev = ans[-1]
            temp = [1 for _ in range(i)]
            for j in range(1, i-1):
                temp[j] = prev[j-1] + prev[j]
            ans.append(temp)
        return ans