class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        ma=0
        mi=0
        n=len(nums)
        for i in range(n):
            if nums[ma]<nums[i]:
                ma=i
            if nums[mi]>nums[i]:
                mi=i
        print(mi,ma)
        x=max(mi,ma)+1
        y=n-min(mi,ma)
        z=min(mi,ma)+n-max(ma,mi)+1
        return min(x,y,z)