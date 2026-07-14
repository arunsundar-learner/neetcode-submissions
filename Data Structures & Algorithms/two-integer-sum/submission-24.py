class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            val=target-nums[i]
            if val in nums[i+1:]: 
                val_02=nums.index(val,i+1)
                return [i,val_02]