class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v = []
        for i in range(len(nums)):
            if nums[i] != val:
                v.append(nums[i])
        nums[:]=v
        return len(v)