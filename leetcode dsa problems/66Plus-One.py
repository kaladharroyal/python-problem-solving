# 66. Plus One
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res = ""
        for i in range(len(digits)):
            res+= str(digits[i])
            print(res)
        res = int(res)+1
        print([int(i) for i in str(res)])

        # return list(str(res))Solution().plusOne([1,2,3]))
Solution().plusOne([1,2,3])
from typing import List    