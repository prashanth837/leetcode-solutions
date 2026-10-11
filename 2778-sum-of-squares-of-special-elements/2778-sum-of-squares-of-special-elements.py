class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        su=0
        for i in range(len(nums)):
            if n%(i+1)==0:
                su+=(nums[i]*nums[i])
        return su
        