class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        dp=[float('-inf')]*(len(nums))
        for i in range(0,len(nums)-1):
            if dp[i-1]==i and nums[i]==0:
                return False
            dp[i]=max(nums[i]+i,dp[i-1])
        print(dp)
        return True if dp[-2]>=len(nums)-1 else False
        