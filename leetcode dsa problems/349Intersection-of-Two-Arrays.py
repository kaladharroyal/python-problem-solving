class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1.intersection(nums2)) 
Solution().intersection([1,2,2,1],[2,2])               