# Time: O(n)
# Space: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        one_present = False
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                one_present = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        if not one_present:
            return 1
        for i in range(n):
            temp = abs(nums[i])
            if temp == n:
                temp = 0
            nums[temp] = -abs(nums[temp])
        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1