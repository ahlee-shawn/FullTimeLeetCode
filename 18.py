# Time: O(n^3) = O(n^(k-1))
# Space: O(n) for sorting & recursion
class Solution:
        
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def kSum(nums, target, k):
            result = []
            
            if not nums:
                return result
            
            average = target // k
            if average < nums[0] or average > nums[-1]:
                return result
            
            if k == 2:
                return twoSum(nums, target)
            
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i+1:], target - nums[i], k-1):
                        result.append([nums[i]] + subset)
            
            return result

        def twoSum(nums, target):
            result = []
            left = 0
            right = len(nums) - 1
            
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum < target or (left > 0 and nums[left] == nums[left - 1]):
                    left += 1
                elif currentSum > target or (right < len(nums) - 1 and nums[right] == nums[right + 1]):
                    right -= 1
                else:
                    result.append([nums[left], nums[right]])
                    left += 1
                    right -= 1
            return result
            
        nums.sort()
        return kSum(nums, target, 4)        