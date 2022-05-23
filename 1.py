# Time: O(n)
# Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        table = dict()
        for i in range(len(nums)):
            if nums[i] in table:
                return [i, table[nums[i]]]
            table[target-nums[i]] = i