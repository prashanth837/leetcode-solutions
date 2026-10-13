class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            a.append(i*i)
        a.sort()
        if len(a)%2==0:
            return sum(a[len(nums)//2:])-sum(a[:len(nums)//2])
        else:
            return sum(a[(len(nums)//2):])-(sum(a[:(len(nums)//2)]))
