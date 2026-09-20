class Solution:
    def reverseDegree(self, s: str) -> int:
        x='abcdefghijklmnopqrstuvwxyz'
        y="0"+x[::-1]
        c=0
        k=1
        for i in range(len(s)):
            c+=(y.index(s[i])*k)
            k+=1
        return c