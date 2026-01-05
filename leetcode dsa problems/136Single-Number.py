class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for ch in nums:
            freq[ch] = freq.get(ch, 0) + 1
        return min(freq, key=freq.get)

Solution().singleNumber([4, 1, 2, 1, 2])