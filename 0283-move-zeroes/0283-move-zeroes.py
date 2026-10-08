class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j=-1
        for i in range(len(nums)):
            if nums[i]!=0:
                j+=1
                nums[j],nums[i]=nums[i],nums[j]
        return nums
        