class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        low=0
        high=len(nums)-1
        ans=[]
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                high=mid-1
            else:
                low=mid+1
        while low<len(nums) and nums[low]==target:
            ans.append(low)
            low+=1
        return ans