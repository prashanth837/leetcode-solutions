class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        c=0
        for i in range(0,len(fl)):
            if len(fl)==1 and fl[0]==0:
                return True if 1>=n else False
            if i==0:
                if fl[i]==0 and fl[1]==0:
                    c+=1
                    fl[0]=1
            if i==len(fl)-1:

                if fl[i]==0 and fl[i-1]==0:
                    c+=1
                    break
            if fl[i]==0 and fl[i-1]==0 and fl[i+1]==0:
                c+=1
                fl[i]=1
        return True if c>=n else False
        

        