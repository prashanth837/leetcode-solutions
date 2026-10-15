class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        su=0
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                x=nums[i:j+1]
                su+=len(set(x))*len(set(x))
        return su
        