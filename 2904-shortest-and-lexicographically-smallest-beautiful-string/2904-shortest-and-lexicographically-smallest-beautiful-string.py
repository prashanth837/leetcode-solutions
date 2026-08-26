class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        min_str=""
        min_len_str=float('inf')
        freq={}
        freq[1]=0
        a=[]
        isvalid=False
        l=0
        if s.count('1')<k:
            return ""
        a=[]
        freq={}
        min_len=float(inf)
        freq[1]=0
        for i in range(len(s)):
            if s[i]=='1':
                freq[1]+=1
            while l<len(s) and freq[1]>=k:
                if freq[1]==k:
                    if i-l+1<=min_len:
                        a.append(s[l:i+1])
                        min_len=i-l+1
                if s[l]=='1':
                    freq[1]-=1
                l+=1
        a.sort()
        mi=float('inf')
        print(a)
        for i in a:
            mi=min(mi,len(i))
        print(mi)
        b=[]
        for i in a:
            if len(i)==mi:
                b.append(i)
        b.sort()
        return b[0]