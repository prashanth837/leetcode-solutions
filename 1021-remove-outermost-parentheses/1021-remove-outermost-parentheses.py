class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        arr=[]
        c1=0
        c2=0
        for i in range(len(s)): 
            stack.append(s[i])
            if s[i]=='(':
                c1+=1
            else:
                c2+=1
            if c1==c2:
                arr.append("".join(stack[1:len(stack)-1]))
                c1=0
                c2=0
                stack=[]
        print(stack)
        return "".join(arr)