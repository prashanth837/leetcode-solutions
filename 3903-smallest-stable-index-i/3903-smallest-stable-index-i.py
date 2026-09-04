class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        ge=[0]*len(nums)
        se=[0]*len(nums)
        ge[0]=nums[0]
        c=0
        se[-1]=nums[-1]
        for i in range(1,len(nums)):
            ge[i]=max(ge[i-1],nums[i])
        for i in range(len(nums)-2,-1,-1):
            se[i]=min(se[i+1],nums[i])
        for i in range(len(nums)):
            if ge[i]-se[i]<=k:
                return i
        return -1