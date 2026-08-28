class Solution:
    def numRabbits(self, ans: List[int]) -> int:
        freq={}
        for i in ans:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        li=[]
        for i,j in freq.items():
            x=i
            y=j
            while y>0:
                if y>x+1:
                    li.append(x+1)
                    y-=(x+1)
                else:
                    li.append(x+1)
                    y=0
        return sum(li)
        
