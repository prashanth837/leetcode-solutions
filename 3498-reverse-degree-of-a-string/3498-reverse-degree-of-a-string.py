class Solution:
    def reverseDegree(self, s: str) -> int:
        x='abcdefghijklmnopqrstuvwxyz'
        y="0"+x[::-1]
        c=0
        k=1
        for i in s: 
            c+=((123-ord(i))*k)
            k+=1
        return c