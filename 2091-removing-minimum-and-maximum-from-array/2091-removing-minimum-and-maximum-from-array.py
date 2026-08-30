class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        ma=0
        mi=0
        for i in range(len(nums)):
            if nums[ma]<nums[i]:
                ma=i
            if nums[mi]>nums[i]:
                mi=i
        print(mi,ma)
        x=max(mi,ma)+1
        y=len(nums)-min(mi,ma)
        z=min(mi,ma)+len(nums)-max(ma,mi)+1
        return min(x,y,z)