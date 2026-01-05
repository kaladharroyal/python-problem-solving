class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            # freq[i] = 1 #this will resets the values in every iteration
            freq[i] = freq.get(i, 0) +1 # this will add the value to the key VALUE
        return max(freq, key =freq.get) 

Solution().majorityElement([1,2,2,3,2,4,2,5,2])    
    
       