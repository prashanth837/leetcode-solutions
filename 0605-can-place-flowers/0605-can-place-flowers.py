class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        temp=[0]+fl+[0]
        c=0
        for i in range(1,len(temp)-1):
            if temp[i]==0 and temp[i-1]==0 and temp[i+1]==0:
                c+=1
                temp[i]=1
            if c>=n:
                return True
        return False
       
        

        