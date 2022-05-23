# Time: O(n^2)
# Space: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)):
            target = -nums[i]
            table = dict()
            for j in range(i+1, len(nums)):
                if nums[j] in table:
                    ans.add(tuple(sorted((nums[i], nums[table[nums[j]]], nums[j]))))
                else:
                    table[target - nums[j]] = j
        return list(ans)