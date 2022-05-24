# Time: O(n)
# Space: O(1)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = -1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= prev:
                prev = nums[i]
            else:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                self.inPlaceReverse(nums, i+1)
                return
        self.inPlaceReverse(nums, 0)
    
    def inPlaceReverse(self, nums, left):
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -=1