class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        b=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                b.append(i)
        return b