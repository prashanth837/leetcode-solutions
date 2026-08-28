class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        freq={}
        li=0
        for i in ans:
            if i==0:
                li+=1
                continue
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        for i,j in freq.items():
            x=i
            y=j
            while y>0:
                if y>x+1:
                    li+=(x+1)
                    y-=(x+1)
                else:
                    li+=(x+1)
                    y=0
        return li
        
