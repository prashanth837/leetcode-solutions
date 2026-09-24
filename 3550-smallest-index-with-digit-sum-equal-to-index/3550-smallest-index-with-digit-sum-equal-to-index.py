class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            su=0
            for j in str(nums[i]):
                su+=int(j)
            if su==i:
                return i
        return -1