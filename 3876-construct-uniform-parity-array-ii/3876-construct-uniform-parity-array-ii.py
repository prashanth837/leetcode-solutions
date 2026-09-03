class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even=True
        odd=True
        for i in nums1:
            if i%2==0:
                odd=False
            else:
                even=False
        nums2=[0]*len(nums1)
        min_odd=float('inf')
        min_odd_index=0
        min_even=float('inf')
        for i in range(len(nums1)):
            if nums1[i]%2!=0:
                if min_odd>nums1[i]:
                    min_odd=nums1[i]
                    min_odd_index=i
            else:
                min_even=min(min_even,nums1[i])
        if even==True:
            return True
        if odd==True:
            return True
        for i in range(len(nums1)):
            if nums1[i]%2!=0:
                nums2[i]=nums1[i]
            else:
                if i!=min_odd_index:
                    if nums1[i]-min_odd>=1:
                        nums2[i]=nums1[i]-min_odd
                    else:
                        return False
        return True
        