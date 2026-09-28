class Solution:
    def maxDepth(self, s: str) -> int:
        a=[]
        ma=0
        for i in s:
            if i=='(':
                a.append('(')
                ma=max(ma,len(a))
            if i==')':
                a.pop()
        return ma

        