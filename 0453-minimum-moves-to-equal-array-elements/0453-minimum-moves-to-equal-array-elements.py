class Solution:
    def minMoves(self, nums: list[int]) -> int:
        x=min(nums)
        su=0
        for i in nums:
            su+=(i-x)
        return su
             