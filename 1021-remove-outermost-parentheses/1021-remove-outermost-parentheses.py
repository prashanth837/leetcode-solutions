class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        c1=0
        for i in s:
            if i=='(':
                if c1>0:
                    stack.append(i)
                c1+=1
            else:
                c1-=1
                if c1>0:
                    stack.append(i)
        return "".join(stack)
