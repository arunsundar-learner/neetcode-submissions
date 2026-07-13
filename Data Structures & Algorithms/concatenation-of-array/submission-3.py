from typing import List

class Solution():
    def getConcatenation(self, nums: List[int])-> List[int]:
        ans=[]
        for i in nums:
            ans.append(i)
        return ans+ans

sol=Solution()
nums=[1,2,1]
print(sol.getConcatenation(nums))