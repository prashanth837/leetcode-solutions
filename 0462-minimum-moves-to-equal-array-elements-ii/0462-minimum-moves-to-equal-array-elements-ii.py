class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        su=0
        if len(nums)%2!=0:
            x=nums[mid]  
        else:
            x=max(nums[mid],nums[mid-1])
        for i in nums:
            su+=abs(x-i)
        return su