class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        a=[0]*len(nums)
        b=[0]*len(nums)
        a[0]=nums[0]
        b[-1]=nums[-1]
        for i in range(1,len(nums)):
            a[i]=max(nums[i],a[i-1])
        for i in range(len(nums)-2,-1,-1):
            b[i]=min(nums[i],b[i+1])
        for i in range(len(nums)):
            if a[i]-b[i]<=k:
                return i
        return -1
        