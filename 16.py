# Time: O(n^2)
# Space: O(n) for sorting
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            currentTarget = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[left] + nums[right]
                if abs(target - ans) > abs(currentTarget - temp):
                    ans = nums[i] + temp
                if temp > currentTarget:
                    right -= 1
                elif temp < currentTarget:
                    left += 1
                else:
                    break
        return ans