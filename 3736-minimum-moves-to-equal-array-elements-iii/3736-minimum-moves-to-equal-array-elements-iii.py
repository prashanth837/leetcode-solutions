class Solution:
    def minMoves(self, nums: List[int]) -> int:
        x=max(nums)
        su=0
        for i in nums:
            su+=abs(x-i)
        return su