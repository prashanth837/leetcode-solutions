class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        a=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if l<=j-i+1<=r:
                    x=sum(nums[i:j+1])
                    if x>0:
                        a.append(x)
        if len(a)>0:
            return min(a)
        else:
            return -1