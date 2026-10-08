class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        res=""
        c1=0
        c2=0
        for i in range(len(s)): 
            stack.append(s[i])
            if s[i]=='(':
                c1+=1
            else:
                c2+=1
            if c1==c2:
                res+="".join(stack[1:len(stack)-1])
                c1=0
                c2=0
                stack=[]
        return res