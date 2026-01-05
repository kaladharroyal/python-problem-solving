class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        for i in range(len(nums)-2):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                return nums[i]
        return nums[-1]        



Solution().repeatedNTimes([1,2,3,3])